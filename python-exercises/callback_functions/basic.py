def greet(name):
    return f"Hello, {name}"

def farewell(name):
    return f"Goodbye, {name}"

def display_message(callback_func, name):
    message = callback_func(name)
    print(message)



display_message(greet, "ege")
display_message(farewell, "ahmet")
