numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]


def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))


def is_odd(x):
    if not x % 2 == 0:
        return True
    else:
        return False
    # return x % 2 != 0


print(list(filter(is_odd, numbers)))
