import os

print(dir(os))  # Printing all functions
print(os.getcwd())  # Printing current directory
os.chdir("D://")  # Changing current directory
print(os.getcwd())
print(os.listdir())  # Printing all files in current directory
# os.mkdir("this") --> Make this folder in current directory
# os.makedirs("this/that") --> Make that folder in this folder in current directory
# os.rename("file", "file2) --> Renames file1 to file2
print(os.environ.get('Path'))  # Printing path environment variable
# os.path.join("D://","/saksham.txt") --> Join the paths
print(os.path.exists("C://"))  # Check whether a path exists or not
print(os.path.isfile("C://"))  # Check whether a file exists or not
print(os.path.isdir("C://"))  # Check whether a directory exists or not
