class Calculator:

    def __init__(self, memory: float=0):
        self.memory = memory

    def addition(self, x: float) -> float:
        self.memory += x
        return self.memory

    def subtraction(self, x: float) -> float:
        self.memory -= x
        return self.memory

    def multiplication(self, x: float) -> float:
        self.memory *= x
        return self.memory

    def division(self, x: float) -> float:
        self.memory /= x
        return self.memory

    def root(self, x: float) -> float:
        self.memory **= 1/x
        return self.memory

    def reset(self) -> float:
        self.memory -= self.memory
        return self.memory

calc = Calculator(0)





