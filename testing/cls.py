class Calc:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    
    def divide(self):
        return self.a / self.b
    

c = Calc(4, 2)

