import os

path = input("Enter path: ")

if os.path.exists(path):
    print(f"this {path}: is a valid path")
    if os.path.isfile:
        print("it is a file")
else:
    print(f"not a valid {path} or not a file or directory")