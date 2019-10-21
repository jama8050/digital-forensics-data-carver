# Digital Forensics Data Carver
Rudimentary data recovery of JPG, PNG, and PDF files with Python 3.

### Features
 * Supports JPG, PNG, and PDF files.
 * Exports the MD5 hashes of found files.
 * Prints basic file information during the carving process.

### Usage
`./cracker.py FILE_NAME` where `FILE_NAME` is the binary file to parse.

### Future Improvements
 * Use the `argparse` library.
 * Improve file detection, reducing false positive detections.
 * Export files by their original names.
 * Deal with non-contiguous files.
 * File integrity checking.
 * More file formats (e.g., GIF, MP4, MOV).

### Credit
This repository was made by Jacob Malcy for CYBR-5830-013, Introduction to Digital Forensics, at CU Boulder.

### License
MIT