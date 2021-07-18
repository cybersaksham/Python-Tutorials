f = open("T19 file write src.txt", "w")
# Deleting whole content & writing this
a = f.write("Saksham is a good boy\n")  # if we store it in variable then that variable returns no of characters written
print("No of letters you wrote are =", a)
f.close()

f = open("T19 file write src.txt", "a")
# Appending new content after present content of file
f.write("Saksham is a good boy\n")
f.close()
