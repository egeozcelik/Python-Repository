def my_decorator(func):
    def wrapper(*args, **kwargs):
        if callable(func):
            print("This function is callable")
            return func(*args, **kwargs)
        else:
            print("Function is not callable")
    return wrapper


@my_decorator
def say_hello(name):
    return f"Hello {name}!"

not_callable = 42


print(say_hello("ege"))
say_hello(not_callable)
