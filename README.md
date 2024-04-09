# Checksum Calculator

## Overview
This Python script calculates the checksum of a file using a specified hashing algorithm. It prompts the user to input the file path and the hashing algorithm, calculates the checksum, and displays the result.

## Requirements
- Python 3.x
- hashlib module (included in Python standard library)

## Usage
### macOS and Linux
1. Clone or download the repository to your local machine.
2. Open a terminal.
3. Navigate to the directory containing the `Checksum.py` file.
4. Run the script using the Python interpreter:

    ```bash
    python3 Checksum.py
    ```

### Windows
1. Clone or download the repository to your local machine.
2. Open Command Prompt.
3. Navigate to the directory containing the `Checksum.py` file.
4. Run the script using the Python interpreter:

    ```cmd
    python Checksum.py
    ```

## Functionality
- **calculate_checksum**: This function calculates the checksum of a file using the specified hashing algorithm. It takes three parameters: `file_path` (path to the file), `algorithm` (hashing algorithm), and `block_size` (optional block size for reading the file).
- **main**: This function serves as the entry point of the script. It prompts the user to input the file path and hashing algorithm, then calls the `calculate_checksum` function to calculate the checksum and print the result.

## Example
```bash
$ python3 Checksum.py
Enter the path to the file: /path/to/your/file.txt
Enter the hashing algorithm to use (e.g., md5, sha1, sha256): sha256

Progress: 100.00% complete
Checksum (sha256): 2b103acb2b87a274c8e8e4a08f3ef35d32f272b8f543372c3638e66c6889ef8c
