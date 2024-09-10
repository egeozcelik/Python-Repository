class Main:
    def __init__(self):
        self.input = None
        name, surname = self.ask_name()
        print("..........................")
        print(f"How do I call you? \n{(name)} or mr.{(surname)} ?")
        

        selection = input('name/pronoun \n')
        if selection == "name":
            print("welcome ", name)
        else:
            print("welcome mr.", surname)
            
    
    def ask_name(self):
        name = input('enter your name.. \n')
        surname = input('enter your surname..\n')
        return name, surname





if __name__ == '__main__':
    main = Main()
    
