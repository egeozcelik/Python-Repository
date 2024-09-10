
import layer2 as ml
class ui_layer:
    def __init__(self):
        self.apply_test()

    def log_results(self, log_params):
        test_name, result, msg = log_params
        if test_name == "":
            print("No test name!")
        else:
            if result:
                print(f"{test_name} test is Successfull. \n{msg}")
            else:
                print(f"{test_name} test is Failed.. \n{msg}")
    def apply_test(self):
        
        ml.middle_layer.test(self.log_results)


if __name__ == "__main__":
    main = ui_layer()