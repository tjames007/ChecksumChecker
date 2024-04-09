import hashlib
import os

def calculate_checksum(file_path, algorithm, block_size=65536):
    """
    Calculate checksum of a file using the specified hashing algorithm.

    Args:
        file_path (str): Path to the file.
        algorithm (str): Hashing algorithm to use (e.g., 'md5', 'sha1', 'sha256').
        block_size (int, optional): Block size for reading the file. Defaults to 65536.

    Returns:
        str: Hexadecimal digest of the calculated checksum.
    """
    # Create hash object based on specified algorithm
    hasher = hashlib.new(algorithm)
    
    # Get size of the file
    file_size = os.path.getsize(file_path)
    
    # Initialize bytes read counter
    bytes_read = 0
    
    # Open the file in binary mode for reading
    with open(file_path, 'rb') as f:
        # Read the file in blocks until the end of the file is reached
        while True:
            data = f.read(block_size)  # Read a block of data from the file
            if not data:  # Check if end of file is reached
                break
            bytes_read += len(data)  # Update bytes read counter
            hasher.update(data)  # Update hash object with read data
            
            # Calculate and display percentage completion
            percent_complete = (bytes_read / file_size) * 100
            print(f"Progress: {percent_complete:.2f}% complete", end='\r')

    # Return hexadecimal digest of the calculated checksum
    return hasher.hexdigest()

def main():
    # Prompt user to input file path
    file_path = input("Enter the path to the file: ")
    
    # Check if file exists
    if not os.path.exists(file_path):
        print("Error: File not found.")
        return
    
    # Prompt user to input hashing algorithm
    algorithm = input("Enter the hashing algorithm to use (e.g., md5, sha1, sha256): ")
    
    # Calculate checksum
    checksum = calculate_checksum(file_path, algorithm)
    
    # Print the calculated checksum
    print(f"\nChecksum ({algorithm}): {checksum}")

if __name__ == "__main__":
    main()
