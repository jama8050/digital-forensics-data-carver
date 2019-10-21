#!/usr/bin/env python3

# Allowed imports by project requirements
from hashlib import md5
from _md5 import md5
import os
import sys

# Magic number for the start and end of JPG, PNG, and PDF files
FILE_MARKERS = {'jpg': (b'\xFF\xD8', b'\xFF\xD9'),
                'png': (b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A', b'\x49\x45\x4E\x44\xAE\x42\x60\x82'),
                'pdf': (b'\x25\x50\x44\x46', b'\x0A\x25\x25\x45\x4F\x46')}
directory_name = "./Malcy"


# Iteration generator for all occurrences of a substr in a major_str
# No return value
# starting_index is used to make sure we don't select end markers that occur before start markers
def find_occurrences(substr, major_str, starting_index):
    # Start search from this location so as not to get duplicates
    start_location = starting_index

    # Loop until no more occurrences of the substr are found
    while start_location != -1:
        yield start_location
        start_location = major_str.find(substr, start_location + 1)


def main():
    # If we're not provided enough arguments, exit with status args
    if len(sys.argv) < 2:
        print("Usage: " + os.path.basename(__file__) + " <file>")
        sys.exit(1)

    # Get the file path
    f_path = sys.argv[1]
    with open(f_path, 'rb') as file_obj:
        data = file_obj.read()

    # Create the folder named "Malcy" if it doesn't exist
    if os.path.isdir(directory_name) is False:
        os.mkdir(directory_name)

    # Used for file names
    file_number = 1

    # Loop through all file types
    for f_type, markers in FILE_MARKERS.items():
        # Accumulator for lines to append to hashes.txt
        lines_to_write = ""

        # For each start file marker, match it with all end markers
        for start_marker in find_occurrences(markers[0], data, 0):
            for end_marker in find_occurrences(markers[1], data, start_marker):

                # Include ALL bytes of the ending marker
                end_marker += len(markers[1]) - 1

                # Carve the file, set its name, export the file
                current_data = data[start_marker:end_marker]
                current_name = "{}/{}.{}".format(directory_name, file_number, f_type)
                with open(current_name, 'wb') as write_obj:
                    write_obj.write(current_data)

                lines_to_write += "{},{}\n".format(current_name, md5(current_data).hexdigest())
                print("{} file found, size of {} bytes, starting offset {}, ending offset {}, exporting as {}"
                      .format(f_type,
                              end_marker - start_marker,
                              hex(start_marker),
                              hex(end_marker),
                              current_name))
                file_number += 1

        # Write out the found hashes
        with open("{}/hashes.txt".format(directory_name), 'a+') as write_obj:
            write_obj.write(lines_to_write)

    print("{} possible files discovered.".format(file_number - 1))


if __name__ == "__main__":
    main()
