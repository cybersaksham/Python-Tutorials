numbers = ["3", "45", "23"]

print("By for loop :-")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(f"number[2] + 1 = {numbers[2] + 1}")

print("By map filter :-")
# map function map over whole list (second arg) & apply first arg.
# map function takes first argument as what to do & second argument as on whom to do.
numbers = list(map(int, numbers))
print(f"number[1] + 1 = {numbers[1] + 1}")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map with lambda is very useful.
square = list(map(lambda x: x * x, num))
print(f"Squares of num is {square}")


def square_func(a):
    return a * a


def cube_func(a):
    return a * a * a


math_list = [square_func, cube_func]
print("List of squares & cube is :-")
for i in range(5):
    val = list(map(lambda x: x(i), math_list))
    print(val)
