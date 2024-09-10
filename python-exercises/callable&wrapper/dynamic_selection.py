def add(x, y):
    return x+y

def multiply(x,y):
    return x * y

operations = [add, multiply, "not callable"]

for operation in operations:
    if callable(operation):
        print(f"result : {operation(10, 5)}")
    else:
        print("not callable")

        