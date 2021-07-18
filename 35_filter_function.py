list1 = [1, 2, 3, 5, 4, 2, 6, 8, 2, 4, 2, 8, 24, 4]


def is_gr_5(num):
    return num > 5


# filter function filter whole list (second arg) for first arg.
# filter function takes first argument as what to do & second argument as on whom to do.
gr_than_5 = list(filter(is_gr_5, list1))
print(gr_than_5)
