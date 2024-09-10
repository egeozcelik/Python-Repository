CALCULATION_MAP = {
    "sum": lambda a, b : a + b,
    "subs": lambda a, b : a - b if a > b else b - a ,
    "multiply": lambda a, b : a*b , 
    "divide" : lambda a, b : a / b if b is not 0 else "N/A"
}

class Backend:
    def __init__(self):
        pass

    def calculate_numbers(self, data_value, operation):
        val1, val2 = data_value
        op = operation

        result = CALCULATION_MAP[operation](data_value)
        print(result)


if __name__ == "__main__":
    main = Backend