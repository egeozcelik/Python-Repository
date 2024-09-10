class Main:
    def __init__(self):
        self.input = None
        value = int(input('enter the value for factorial \n'))
        self.factorial = value
        result = self.factorial_calculator(value)
        print("result : ", result)
       
    def factorial_calculator(self,_value):
        fac = _value
        while _value > 1:
            _value = _value - 1
            fac = fac * _value 
        return fac

if __name__ == "__main__":
    main = Main()