def multi(*args):
    total = 1
    for i in args:
        total *= i
    return total


total = multi(1, 2, 3, 4, 5)
print(total)
