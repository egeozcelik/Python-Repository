#
my_lambda = lambda x: x+10

print(callable(my_lambda))
print(my_lambda(5))

##
sqrt = lambda x: x*x
print(sqrt(5))



###
def print1():
    return "hello"

def print2():
    return "world"

quote = lambda x: print1() + " " + print2() + str(x)

print(quote(" ege ozcelik"))
