# DESCRIPTION:
# Write a function that given, an array arr, returns an array containing at each index i the amount of numbers that are smaller than arr[i] to the right.

# For example:

# * Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
# * Input [1, 2, 0] => Output [1, 1, 0]


class Main:
    def __init__(self):
        my_arr = [5,4,3,2,1]
        result = self.array_calculator(my_arr)
        print("result : ", result)
    def array_calculator(self,arr):
        result_arr = []

        for index, num in enumerate(arr):
            current_index = index
            counter = 0
            
            while current_index < len(arr):
                if num > arr[current_index]:
                    counter = counter + 1
                current_index = current_index + 1
            
            result_arr.append(counter)
            
        return result_arr

if __name__ == "__main__":
    main = Main()

