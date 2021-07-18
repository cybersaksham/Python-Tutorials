r = open("T18 file read src.txt")
content = r.read()  # Storing file data in variable

print("The file r \"T18 file read src.txt\" contains :-")
print(content)
print()

r.close()  # It is a good practice to close a file so that other programs can use that file

rb = open("T18 file read src.txt", "rb")  # Opening in binary mode
content = rb.read()

print("The file rb \"T18 file read src.txt\" contains :-")
print(content)
print()

rb.close()

rt = open("T18 file read src.txt", "rt")  # Opening in text mode - default
content = rt.read(3)  # Storing first 3 characters of file

print("The file rt \"T18 file read src.txt\" contains :-")
print(content)
content = rt.read(3)  # Storing next 3 characters of file
print(content)
print()

rt.close()

line1 = open("T18 file read src.txt", "rt")
content = line1.read()  # Read all characters one by one

print("The file line1 \"T18 file read src.txt\" contains :-")
for line in content:
    print(line)
print()

line1.close()

line2 = open("T18 file read src.txt", "rt")  # Read all lines one by one

print("The file line2 \"T18 file read src.txt\" contains :-")
for line in line2:
    print(line, end="")
print()
print()

line2.close()

readline1 = open("T18 file read src.txt", "rt")

print("The file readline1 \"T18 file read src.txt\" contains :-")
print(readline1.readline(), end="")  # Reading first line
print(readline1.readline(), end="")  # Reading next line
print()

readline1.close()

readlines1 = open("T18 file read src.txt", "rt")

print("The file readlines1 \"T18 file read src.txt\" contains :-")
print(readlines1.readlines(), end="")  # Read all lines at once
print()

readlines1.close()
