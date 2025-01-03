"""This module includes all the calculator exceptions """


# Exception for invalid factorial argument (non (positive-integer))
class FactorialArgumentError(Exception):
    def __init__(self, argument):
        self._argument = argument

    def __str__(self):
        return (
            "Factorial Error: Factorial on a non positive-integer '%s' is undefined."
            % self._argument
        )

    def get_argument(self):
        return self._argument


# Exception for invalid hashtag (applied to negative numbers)
class HashtagArgumentError(Exception):
    def __init__(self, argument):
        self._argument = argument

    def __str__(self):
        return (
            "Hashtag Error: Hashtag on a negative value '%s' is undefined."
            % self._argument
        )

    def get_argument(self):
        return self._argument


# Exception for invalid fraction power on negative base
class PowerByFractionError(Exception):
    def __init__(self, base, power):
        self._base = base
        self._power = power

    def __str__(self):
        return (
            "Power By Fraction Error: Fraction power '%s' on a negative base '%s' is undefined."
            % (self._power, self._base)
        )

    def get_base(self):
        return self._base

    def get_power(self):
        return self._power


# Exception for a non-positive power on a zero base
class ZeroPowerError(Exception):
    def __init__(self, power):
        self._power = power

    def __str__(self):
        return (
            "Zero Power Error: non-positive power '%s' on a zero base '0' is undefined."
            % self._power
        )

    def get_base(self):
        return 0

    def get_power(self):
        return self._power


# Exception for missing operand in the expression
class MissingOperandError(Exception):
    def __init__(self, operator):
        self._operator = operator

    def __str__(self):
        return (
            "Missing Operand Error: You need two numbers to operate '%s'."
            % self._operator
        )

    def get_operator(self):
        return self._operator


# Exception for missing operator in the expression
class MissingOperatorError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Missing Operator Error: There are missing operators between the expression values."


# Exception for invalid first character in the expression
class InvalidFirstCharError(Exception):
    def __init__(self, first_char):
        self._first_char = first_char

    def __str__(self):
        return (
            "First Char Error: The first character '%s' is not valid. "
            "It must be a digit, '(' , '-' , or '~'."
            % self._first_char
        )

    def get_first_char(self):
        return self._first_char


# Exception for an empty expression
class EmptyExpressionError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Empty Expression Error: The expression is empty."


# Exception for invalid character sequence
class InvalidSequenceError(Exception):
    def __init__(self, first_char, second_char):
        self._first_char = first_char
        self._second_char = second_char

    def __str__(self):
        return (
            "Sequence Error: The sequence '%s' '%s' is not valid. "
            "Operators and dots cannot appear in a sequence, except for: "
            "parentheses, minuses and right unary operators"
            % (self._first_char, self._second_char)
        )

    def get_first_char(self):
        return self._first_char

    def get_second_char(self):
        return self._second_char


# Exception for invalid dot placement in the expression
class DotPlacementError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Dot Placement Error: A dot cannot appear before or after '%s'. "
            "It should only appear before a value or after a value/operator or '(' ."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid surrounding dots
class SurroundingDotsError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Surrounding Dots Error: A value '%s' cannot be surrounded by two dots. Dots should only appear before "
            "or after a value."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid character in the expression
class InvalidCharError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Invalid Char Error: The character '%s' is invalid. "
            "Only digits, operators, parentheses, and dots are allowed."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid unary-minus usage
class InvalidUnaryMinusError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Invalid Unary Minus Error: Unary minus cannot be applied to '%s'. "
            "It must appear before a digit, '(', or '-'."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid binary-minus usage
class InvalidBinaryMinusError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Invalid Binary Minus Error: Binary minus cannot be applied to '%s'. "
            "It must appear before a digit, '(', '-' or '~' ."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid sign-minus usage
class InvalidSignMinusError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Invalid Sign Minus Error: Sign minus cannot be applied to '%s'. "
            "It must appear before a digit, '(', or '-'."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid usage of tilde after an invalid character
class TildeAfterInvalidError(Exception):
    def __init__(self, prev_char):
        self._prev_char = prev_char

    def __str__(self):
        return (
            "Tilde After Invalid Error: '~' cannot follow '%s'. "
            "It must follow an operand, '(' or '-'."
            % self._prev_char
        )

    def get_pprev_char(self):
        return self._prev_char


# Exception for invalid usage of tilde before an invalid character
class TildeBeforeInvalidError(Exception):
    def __init__(self, next_char):
        self._next_char = next_char

    def __str__(self):
        return (
            "Tilde Before Invalid Error: '~' cannot appear before a value/expression with '%s'. "
            "It must appear before a digit, '-', or '('."
            % self._next_char
        )

    def get_next_char(self):
        return self._next_char


# Exception for invalid single-character expression
class InvalidSingleCharError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Invalid Single Char Error: '%s' is a single invalid character. "
            "Only numbers can stand alone."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid last character in the expression
class InvalidLastCharError(Exception):
    def __init__(self, last_char):
        self._last_char = last_char

    def __str__(self):
        return (
            "Invalid Last Char Error: The last character '%s' is invalid. "
            "The last character must be a digit, '!', '#' or ')'"
            % self._last_char
        )

    def get_last_char(self):
        return self._last_char


# Exception for mismatched parentheses in the expression
class MismatchedParenthesesError(Exception):
    def __init__(self, open_parentheses, close_parentheses):
        self._open_parentheses = open_parentheses
        self._close_parentheses = close_parentheses

    def __str__(self):
        return (
            "Mismatched Parentheses Error: There are %d opening parentheses '(' and %d closing parentheses ')'. "
            "They must be balanced."
            % (self._open_parentheses, self._close_parentheses)
        )

    def get_open_parentheses_count(self):
        return self._open_parentheses

    def get_close_parentheses_count(self):
        return self._close_parentheses


# Exception for invalid character right after a parenthesis
class InvalidCharAfterParenthesisError(Exception):
    def __init__(self, invalid_char):
        self._invalid_char = invalid_char

    def __str__(self):
        return (
            "Invalid Char After Parenthesis Error: '%s' cannot follow '('. "
            "Only digits, '(' , `~` or '-' can follow '(' ."
            % self._invalid_char
        )

    def get_invalid_char(self):
        return self._invalid_char


# Exception for invalid character right before a right unary operator
class InvalidCharBeforeRightOperatorError(Exception):
    def __init__(self, invalid_char, right_operator):
        self._invalid_char = invalid_char
        self._right_operator = right_operator

    def __str__(self):
        return (
            "Invalid Char Before Right Operator Error: '%s' cannot appear before '%s'. "
            "Only digits, '-' , or right unary operators can appear before right unary operators ."
            % (self._invalid_char, self._right_operator)
        )

    def get_invalid_char(self):
        return self._invalid_char
