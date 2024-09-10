import requests
class Excersize:
    def __init__(self):
        value = "https://w3schools.com/python/demopage.htm"
        self.split_sentence(value=value)


    def split_sentence(self, value):
        x = requests.get(value)
        print(x.text)


if __name__ == "__main__":
    main = Excersize()