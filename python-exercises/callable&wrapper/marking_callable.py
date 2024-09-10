from typing import Any


class MathOperations:
    def __init__(self, _operation):
        self.operation = _operation
    
    def __call__(self, x,y):
        if self.operation == "add":
            return x + y
        elif self.operation == "multiply":
            return x*y
        else:
            raise ValueError("Invalid Selection for Math Operations")
        


adder = MathOperations("add")
multiplier = MathOperations("multiply")

print(adder(5, 10))
print(multiplier(2, 9))

##MathOperations class'ı __call__ sayesinde bir fonksiyon gibi çağırılabilir. kendinden türetilen adder ve multiplier objelerini fonksiyon gibi kullanabiliyoruz.
