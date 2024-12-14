
class FactorialArgumentError(Exception):
    def __init__(self, argument):
        self._argument = argument

    def __str__(self):
        return "Factorial Error: Factorial on a non positive-integer '%s' is undefined." % self._argument

    def get_argument(self):
        return self._argument


class HashtagArgumentError(Exception):
    def __init__(self, argument):
        self._argument = argument

    def __str__(self):
        return "Hashtag Error: Hashtag on a negative value '%s' is undefined." % self._argument

    def get_argument(self):
        return self._argument


class PowerArgumentError(Exception):
    def __init__(self, base, power):
        self._base = base
        self._power = power

    def __str__(self):
        return "Power Error: Fraction power '%s' on a negative base '%s' is undefined." % (self._power, self._base)

    def get_base(self):
        return self._base

    def get_power(self):
        return self._power


class TooManyOperatorsError(Exception):
    def __init__(self, operator):
        self._operator = operator

    def __str__(self):
        return "Too Many Operators Error: You need two numbers to operate '%s'." % self._operator

    def get_operator(self):
        return self._operator


class NotEnoughOperatorsError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Not Enough Operators Error: There are not enough operators between the expression values."






class FirstCharError(Exception):
    def __init__(self, first_char):
        self._first_char = first_char

    def __str__(self):
        return "First Char Error: The first character '%s' is not valid. It must be a digit, '(' , '-' , or '~'." % self._first_char

    def get_first_char(self):
        return self._first_char


class EmptyExpressionError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Empty Expression Error: The expression is empty."


class SequenceError(Exception):
    def __init__(self, first_char, second_char):
        self._first_char = first_char
        self._second_char = second_char

    def __str__(self):
        return ("Sequence Error: The sequence '%s' '%s' is not valid. "
                "Operators and dots cannot appear in a sequence, except for: '-', '!', or '#'." % (self._first_char, self._second_char))

    def get_first_char(self):
        return self._first_char

    def get_second_char(self):
        return self._second_char


class DotPlacementError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return "Dot Placement Error: A dot cannot appear before or after '%s'. It should only appear before or after a value." % self._invalid_char

    def get_invalid_char(self):
        return self._invalid_char


class SurroundingDotsError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return "Surrounding Dots Error: A value '%s' cannot be surrounded by two dots. Dots should only appear before or after a value." % self._invalid_char

    def get_invalid_char(self):
        return self._invalid_char


class InvalidCharError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return "Invalid Char Error: The character '%s' is invalid. Only digits, operators, parentheses, and dots are allowed." % self._invalid_char

    def get_invalid_char(self):
        return self._invalid_char


class InvalidUnaryMinusError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return "Invalid Unary Minus Error: Unary minus cannot be applied to '%s'. It must appear before a digit, '(', or '-'." % self._invalid_char

    def get_invalid_char(self):
        return self._invalid_char


class TildeAfterInvalidError(Exception):
    def __init__(self, prev_char):
        self._prev_char = prev_char

    def __str__(self):
        return "Tilde After Invalid Error: '~' cannot follow '%s'. It must follow an operand, '(' or '-'." % self._prev_char

    def get_pprev_char(self):
        return self._prev_char


class TildeBeforeInvalidError(Exception):
    def __init__(self, next_char):
        self._next_char = next_char

    def __str__(self):
        return "Tilde Before Invalid Error: '~' cannot appear before '%s'. It must appear before a digit, '-', or '('." % self._next_char

    def get_next_char(self):
        return self._next_char


class InvalidSingleCharError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return "Invalid Single Char Error: '%s' is a single invalid character. Only numbers can stand alone." % self._invalid_char

    def get_invalid_char(self):
        return self._invalid_char


class InvalidLastCharError(Exception):
    def __init__(self, last_char):
        self._last_char = last_char

    def __str__(self):
        return "Invalid Last Char Error: The last character '%s' is invalid. The last character must be a digit, '!', or ')'" % self._last_char

    def get_last_char(self):
        return self._last_char


class MismatchedParenthesesError(Exception):
    def __init__(self, open_parentheses, close_parentheses):
        self._open_parentheses = open_parentheses
        self._close_parentheses = close_parentheses

    def __str__(self):
        return "Mismatched Parentheses Error: There are %d opening parentheses '(' and %d closing parentheses ')'. They must be balanced." % (self._open_parentheses, self._close_parentheses)

    def get_open_parentheses_count(self):
        return self._open_parentheses

    def get_close_parentheses_count(self):
        return self._close_parentheses

