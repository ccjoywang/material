from functools import reduce
numbers = [-1, 0, 1, 2]


def add(x, y):
    return x + y


print(reduce(add, numbers, 5))

words = ['Hello', 'World']


def join_strings(strings):
    return reduce(lambda x, y: x + ' ' + y, strings, 'Joy')


print(join_strings(words))
