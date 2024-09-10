def calculate(expression ,x, y):
    return expression(x, y)



print(calculate(lambda x,y: x*y, 4, 5))
print(calculate(lambda x,y: x- y, 4, 5))

