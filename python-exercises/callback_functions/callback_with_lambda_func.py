def calculate(operation, a,b):
    return operation(a,b)


result = calculate(lambda x, y: x + y, 10, 5)
print(result)

result = calculate(lambda x, y: x * y, 4, 8)
print(result)
