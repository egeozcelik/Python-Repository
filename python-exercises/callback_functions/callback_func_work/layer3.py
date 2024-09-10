class backend:
    def __init__(self, callback_func) -> None:
        self.cb = callback_func
        self.start_process()


    def start_process(self):
        self.cb({"CAN", False, "The CAN test was failed."})
        
        self.cb({"", True, "asd"})

        self.cb({"ethernet", True, "The ethernet test was succesfully maded."})