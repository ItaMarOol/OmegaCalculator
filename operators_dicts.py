from operators import *

class OperatorsPriorities:
    def __init__(self):
        self.operators_priorities = {"+" : 1, "-" : 1, "*" : 2, "/":2,
                                     "u":2.5, "^": 3, "%": 4, "$": 5,
                                     "&": 5, "@": 5, "~": 6, "!": 6, "#":6, "s" : 100}

    def get_priority(self, operator : str):
        return self.operators_priorities.get(operator, -1)


class OperatorsPlacements:
    def __init__(self):
        self.operators_placements_dictionary = {"+" : "Middle", "-" : "Middle", "*" : "Middle", "/": "Middle",
                                     "u": "Left", "^": "Middle", "%": "Middle", "$": "Middle",
                                     "&": "Middle", "@": "Middle", "~": "Left", "!": "Right", "#": "Right", "s" : "Left"}

    def get_placement(self, operator : str):
        return self.operators_placements_dictionary.get(operator, -1)

class OperatorsClasses:
    def __init__(self):
        self.operators_classes_dictionary = {"+" : Addition, "-" : Subtraction, "*" : Multiplication, "/":Division,
                                     "u":UnaryMinus, "^": Power, "%": Modulo, "$": Maximum,
                                     "&": Minimum, "@": Average, "~": Tilde, "!": Factorial, "#": Hashtag, "s": SignMinus}

    def get_class(self, operator : str):
        return self.operators_classes_dictionary.get(operator, -1)
