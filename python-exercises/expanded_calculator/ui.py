from expanded_calculator.backend import Backend as service

class UI:
    def __init__(self):
        tupple_val = 15,2
        service.calculate_numbers(tupple_val, "sum")