"""This module includes the calculator operators dictionaries. """
from operators import *


class OperatorsPriorities:
    """This class includes a dictionary with the calculator operators and their priorities."""

    def __init__(self):
        self.priorities_dict = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "u": 2.5,
            "^": 3,
            "%": 4,
            "$": 5,
            "&": 5,
            "@": 5,
            "~": 6,
            "!": 6,
            "#": 6,
            "s": 100,
        }

    def get_priority(self, operator: str):
        return self.priorities_dict.get(operator, -1)


class OperatorsPlacements:
    """This class includes a dictionary with the calculator operators and their placements."""

    def __init__(self):
        self.placements_dict = {
            "+": "Middle",
            "-": "Middle",
            "*": "Middle",
            "/": "Middle",
            "u": "Left",
            "^": "Middle",
            "%": "Middle",
            "$": "Middle",
            "&": "Middle",
            "@": "Middle",
            "~": "Left",
            "!": "Right",
            "#": "Right",
            "s": "Left",
        }

    def get_placement(self, operator: str):
        return self.placements_dict.get(operator, -1)


class OperatorsClasses:
    """This class includes a dictionary with the calculator operators and their classes."""

    def __init__(self):
        self.classes_dict = {
            "+": Addition,
            "-": Subtraction,
            "*": Multiplication,
            "/": Division,
            "u": UnaryMinus,
            "^": Power,
            "%": Modulo,
            "$": Maximum,
            "&": Minimum,
            "@": Average,
            "~": Tilde,
            "!": Factorial,
            "#": Hashtag,
            "s": SignMinus,
        }

    def get_class(self, operator: str):
        return self.classes_dict.get(operator, -1)
