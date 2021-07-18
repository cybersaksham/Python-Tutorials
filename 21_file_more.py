f = open("T21 file more src.txt", "r+")
print("File handle is at position", f.tell())  # Tell that at which index our pointer is right now
print(f.readline())  # This read one line so index of pointer changed - refer next line
print("File handle is at position", f.tell())
print(f.readline())
print("File handle is at position", f.tell())

f.seek(5)  # Resetting index of pointer to given argument
print("File handle is reset to position", f.tell())
print(f.readline())

f.close()
