def my_decorator(func):
    def wrapper():
        print("before the function called")
        func()
        print("after the function called")
    return wrapper

@my_decorator
def say_hello():
    print("Merhaba!")


say_hello()

# Decorator, Python'da kullanılan fonksiyonların veya metodların davranışlarını değiştirmek veya genişletmek için kullanılan yapıdır.
# Bir decorator, bir fonksiyonu alır, ona bazı ek işlemler uygular ve ardından yeni bir fonksiyon döner. bu işlemi gerçekleştiren iç fonksiyona wrapper denir.

# my_decorator adlı decorator fonksiyonu, bir fonksiyonu (bu durumda 'say_hello') alır ve onu sarmalar(wrap)
# Wrapper fonksiyonu aslında sarmalanan wrapped fonksiyonudur. func() fonksiyonu, bu wrapper içinde çağırılır ve çevresinde ek işlemler yapılır.
# @my_decorator ifadesi, say_hello() fonksiyonunu my_decorator ile sarmalayarak ona ek davranışlar kazandırır.

# PARAMETRE ALAN BİR DECORATOR

def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("before the function called")
        result = func(*args, **kwargs)
        print("after the function called")
        return result
    return wrapper

@my_decorator2
def say_hello2(name):
    print(f"Merhaba, {name}!")


say_hello2("ege")