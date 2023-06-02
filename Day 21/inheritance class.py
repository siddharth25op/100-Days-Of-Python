####### First class #######
class Pokemon:
    def __init__(self):
        self.a = 10
        self.b = 10


####### Second class that inherits First class #######
class Pikachu(Pokemon):
    
    def sum(self):
        super().__init__()
        sum_of = self.a + self.b
        print(sum_of)


Pikachu().sum()
