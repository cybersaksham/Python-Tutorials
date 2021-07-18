"""
Break --> For exiting the loop & execute code after the loop
Continue --> For exiting the current loop & re-enter in it
"""

i = 0
j = 0

while (True):
    print(i, end=" ")
    if i == 50:
        break
    i = i + 1

print("")

while (1):
    j = j + 1
    if j < 5:
        continue
    print(j, end=" ")
    if j == 50:
        break
