class Calculator:

    def __init__(self, memory:float=0):
        self.memory = memory

    def addition(self, x: float) -> float:
        ''' takes a float and adds this float to the memory, which is set to 0
            and returns new float, which is stored in memory (until reset):
            For example:
            >>>calc.addition(5)
            5
            
        '''
        self.memory += x
        return self.memory

    def subtraction(self, x: float) -> float:
        ''' takes a float and subtracts this float of the memory, which was set to 5
            after addtion and returns new float, which is stored in memory (until reset):
            For example:
            >>>calc.subtraction(2)
            3
            
        '''
        self.memory -= x
        return self.memory

    def multiplication(self, x: float) -> float:
        ''' takes a float and multiplies memory (was set to 3 after subtraction) by this float
            and returns new float, which is stored in memory (until reset):
            For example:
            >>>calc.multiplication(18)
            54
            
        '''
        self.memory *= x
        return self.memory

    def division(self, x: float) -> float:
        ''' takes a float and divides memory (was set to 54 after multiplication) by this float
            and returns new float, which is stored in memory (until reset):
            For example:
            >>>calc.addition(2)
            27
            
        '''
        self.memory /= x
        return self.memory

    def root(self, x: float) -> float:
        ''' takes a float and takes root of this float from memory (was set to 27 after division)
            and returns new float, which is stored in memory (until reset):
            For example:
            >>>calc.addition(3)
            3
            
        '''
        self.memory **= 1/x
        return self.memory

    def reset(self) -> float:
        ''' resets calculator's memory (which was 3 after root function) to 0
            For example:
            >>>calc.reset()
            0
            
        '''
        self.memory -= self.memory
        return self.memory
