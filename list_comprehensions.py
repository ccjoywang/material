numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print([n for n in numbers if n > 0])

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print([n for n in numbers if n % 2 == 0])

words = ["hello", "my", "name", "is", "Sam"]
print([(w, len(w)) for w in words])
