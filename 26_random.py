import random  # This is module for find random numbers.

random_int = random.randint(0, 100)  # Find random integer b/w 0 & 100 both included
random_number = random.random()  # Find random number from 0 to 1 & multiply it by n if you want from 0 to n
print("random integer b/w 0 & 100 both included is", random_int)
print("random number b/w 0 & 100 both included is", random_number * 100)

list = ["saksham", "shubham", "harry", "rohan"]
choice = random.choice(list)  # Chooses a random element from a list
print("random choice from list is", choice)
