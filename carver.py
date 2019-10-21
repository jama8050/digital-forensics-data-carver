#!/usr/bin/env python3

# Allowed imports by project requirements
import binascii
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
    # Create the folder named "Malcy" if it doesn't exist
    if os.path.isdir(directory_name) is False:
        os.mkdir(directory_name)

    # TODO: Parse cmdline arguments


if __name__ == "__main__":
    main()
