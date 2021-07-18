import time

initial = time.time()  # For present time

for i in range(200):
    print("This is saksham")
print(f"For loop run in {time.time() - initial} seconds\n")

k = 0
while k < 200:
    print("This is harry")
    k = k + 1
print(f"While loop run in {time.time() - initial} seconds\n")

# For printing day, month, date, time up to seconds, year at present
print(f"Time now is {time.asctime(time.localtime(time.time()))}\n")

for i in range(5):
    print("This will print in interval of 1 second")
    time.sleep(1)  # For taking a gap
