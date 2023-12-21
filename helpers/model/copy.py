from utilities import *

# Function to smartly copy a file from a remote location to a local path
def smart_copy(remote_path, local_path):
    # Open the remote file in binary write mode
    with open(remote_path, "wb") as remote_file:
        # Open the local file in binary read mode
        with open(local_path, "rb") as local_file:
            # Read the content of the local file and write it to the remote file
            remote_file.write(local_file.read())
