str1 = "Saksham is a good boy"
str2 = "Sakshamisagoodboy"
str3 = "saksham is a good boy"

print("str1 = " + str1)
print("str1[0] = " + str1[0])
print("str1[1] = " + str1[1])
print("str1[0:5] = " + str1[0:5])
print("Length of str1 is " + str(len(str1)))
print("str1[0:90] = " + str1[0:90])
print("str1[0:] = " + str1[0:])  # Second argument is total length by default
print("str1[:5] = " + str1[:5])  # First argument is 0 by default
print("str1[::] = " + str1[::])  # Third argument is 1 by default
print("str1[0:21:2] = " + str1[0:90:2] + " \"Here 2 is jump\"")
print("str1[0::555] = " + str1[0::555])
print("str1[-5:] = " + str1[-5:])
print("str1[-5:-2] = " + str1[-5:-2])
print("str1[::-1] = " + str1[::-1])
print("str1[::-2] = " + str1[::-2])

print("is str1 contain only alpha-numerics - " + str(str1.isalnum()))  # Check all chaarcters are alpha-numeric
print("is str2 contain only alpha-numerics - " + str(str2.isalnum()))

print("is str1 contain only alphabetic - " + str(str1.isalpha()))  # Check all characters are alphabetic
print("is str2 contain only alphabetic - " + str(str2.isalpha()))

print("is str1 is ending with boy - " + str(str1.endswith("boy")))  # Check ending with argument given

print("Number of s time in str1 is - " + str(str1.count("s")))  # Count no. of occurence of a substring
print("Number of space time in str1 is - " + str(str1.count(" ")))

print("After first letter capitalize of str3 - " + str(str3.capitalize()))  # Capitalize first letter

print("Index of is in str1 - " + str(str1.find("is")))  # Find index of a substring

print("Lower case of str1 is - " + str(str1.lower()))  # Convert whole string into lower case
print("Upper case of str1 is - " + str(str1.upper()))  # Convert whole string into upper case

print("After replace is by are in str1 - " + str(str1.replace("is", "are")))  # Replace first item by second
