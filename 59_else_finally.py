f = open("T18 file read src.txt")

try:
    f1 = open("saksham.txt")

except Exception as e:
    print(e)

else:
    print("This will run only when except is not running")

finally:
    print("This will run when try or except either is running")
    # f1.close()
    f.close()

print("This is important line")
