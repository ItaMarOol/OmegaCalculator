from operators import *

class OperatorsPriority:
    def __init__(self):
        self.operators_dictionary = {'+' : 1, '-' : 1, '*' : 2, '/':2,
                                     'u':2.5, '^': 3, '%': 4, '$': 5,
                                     '&': 5, '@': 5, '~': 6, '!': 6}

    def get_priority(self, operator):
        return self.operators_dictionary.get(operator, -1)

class OperatorsClasses:
    def __init__(self):
        self.operators_class_dictionary = {'+' : Addition, '-' : Subtraction, '*' : Multiplication, '/':Division,
                                     'u':UnaryMinus, '^': Power, '%': Modulo, '$': Maximum,
                                     '&': Minimum, '@': Average, '~': Tilde, '!': Factorial}

    def get_class(self, operator):
        return self.operators_class_dictionary.get(operator, -1)