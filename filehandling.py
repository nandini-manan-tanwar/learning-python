import os
file_path="testing"


if os.path.exists(file_path):
    print(f"this file exist at '{file_path}'")
    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isdir(file_path):
        print("it is a directory")
else:
    print("file don't exist")