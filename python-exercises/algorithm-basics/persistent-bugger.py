# DESCRIPTION:
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
# 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)


class Main:
    def __init__(self) -> None:
        calc = 93979
        # print(f"total digit count = {(self.dizi_basamak_kontrol(calc))}")
        # print(f"total digit multiplied = {(self.dizi_basamaklarini_carp(calc))}")
        self.calculate(calc)

    def dizi_basamak_kontrol(self, num):
        counter = 0
        while int(num) > 0:
            num = num / 10
            counter += 1
        return counter

    def calculate(self, num):
        control = num
        while self.dizi_basamak_kontrol(control) > 1:
            control = self.dizi_basamaklarini_carp(control)
        print(control)
        

    def dizi_basamaklarini_carp(self, num):
        my_arr = []
        while int(num) > 0:
            my_arr.append(num % 10)
            num = int(num / 10)
        res = 1
        for i in my_arr:
            res = res * i
        
        print(f"{res}")
        return res
            



        


if __name__ == "__main__":
    main = Main()



#DIGIT COUNTER
        # counter = 1
        # temp = num
        # while int(temp / 10) > 0:
        #     counter = counter + 1
        #     temp = int(temp/10)
        # print("digit count: ", counter)


#FOR ONLY 2 DIGITS

        # while int(num / 10) > 0:
        #     result = int(num / 10) * int(num % 10)
        #     num = result
        # return num