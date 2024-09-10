from typing import Any


class MyCallableClass:
    def __call__(self, args):
        return args*5
    
class NonCallableClass:
    def __init__(self) -> None:
        print("hello")

obj = MyCallableClass()
obj2 = NonCallableClass()


print(callable(obj)) #true
print(obj(10)) #50
print(callable(obj2)) #false

