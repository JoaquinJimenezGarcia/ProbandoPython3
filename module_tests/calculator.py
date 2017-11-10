class Calculator():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def set_numero1(self, numero1):
        self.numero1 = numero1

    def set_numero2(self, numero2):
        self.numero2 = numero2

    def add(self):
        return self.numero1 + self.numero2

    def minus(self):
        return self.numero1 - self.numero2