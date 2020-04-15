numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(list(filter(lambda x: x % 3 == 0, numbers)))

# Linter Converts the lambda to def automatically


def condition(x): return x % 3 != 0


print(list(filter(condition, numbers)))
print(list(map(condition, numbers)))
