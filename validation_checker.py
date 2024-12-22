"""This module handling the initial mathematical-expression validation check."""
from exceptions import (
    EmptyExpressionError,
    InvalidFirstCharError,
    InvalidCharError,
    InvalidSequenceError,
    DotPlacementError,
    InvalidSingleCharError,
    InvalidUnaryMinusError,
    TildeBeforeInvalidError,
    TildeAfterInvalidError,
    InvalidLastCharError,
    MismatchedParenthesesError,
    SurroundingDotsError,
    InvalidSignMinusError,
    InvalidBinaryMinusError,
    InvalidCharAfterParenthesisError,
    InvalidCharBeforeRightOperatorError,
)
from operators_dicts import OperatorsPriorities, OperatorsPlacements


class ValidationChecker:
    """This class responsible for validating mathematical expressions."""

    def __init__(self):
        self.ops_priorities = OperatorsPriorities()
        self.ops_placements = OperatorsPlacements()
        self.left_parenthesis_counter = 0
        self.right_parenthesis_counter = 0

    def is_valid_expression_check(self, infix_str_expression: str) -> bool:
        """
        This function checks if a given infix mathematical expression is valid.

        :param infix_str_expression: mathematical expression in infix order
        :return: True if the expression is valid. else - raises an informative exception
        """

        # removing white spaces
        expression = infix_str_expression.replace(" ", "").replace("\t", "")
        self.left_parenthesis_counter = 0
        self.right_parenthesis_counter = 0

        self.initial_check(expression)
        self.minus_check(expression)
        self.tilde_check(expression)
        self.char_placements_check(expression)
        self.operators_sequence_check(expression)
        self.dots_check(expression)
        self.parenthesis_check(expression)

        return True

    def initial_check(self, expression: str):
        """
        This function is the initial check of the expression. It checks empty expression, invalid first char, invalid last char, invalid char.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """
        # empty input check
        if expression == "":
            raise EmptyExpressionError()

        # invalid first char check
        char = expression[0]
        if not (
            char.isdigit() or char == "(" or char == "-" or char == "~" or char == "."
        ):
            raise InvalidFirstCharError(char)

        # Invalid last char check
        if not (
            expression[-1].isdigit()
            or self.ops_placements.get_placement(expression[-1]) == "Right"
            or expression[-1] == ")"
        ):
            raise InvalidLastCharError(expression[-1])

        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index].
            # invalid char check
            if not (
                char.isdigit()
                or char in self.ops_priorities.priorities_dict
                or char == "("
                or char == ")"
                or char == "."
            ):
                raise InvalidCharError(char)

    def minus_check(self, expression: str):
        """
        This function checks that the minuses in the expression are valid.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """

        sign_minus_flag = 0
        unary_minus_flag = 0
        minus_flag = 0

        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index].
            # minus check
            if char == "-":
                if index == 0 or expression[index - 1] == "(":
                    unary_minus_flag = 1
                elif (
                    expression[index - 1] in self.ops_priorities.priorities_dict
                    and self.ops_placements.get_placement(expression[index - 1])
                    != "Right"
                ):
                    sign_minus_flag = 1
                else:
                    minus_flag = 1

                if index + 1 < len(expression):
                    while index + 1 < len(expression) and expression[index + 1] == "-":
                        index += 1
                        if unary_minus_flag == 0:  # not unary minus sequence
                            sign_minus_flag = 1
                    if not (
                        expression[index + 1].isdigit()
                        or expression[index + 1] == "-"
                        or expression[index + 1] == "("
                        or expression[index + 1] == "."
                    ):  # invalid char after a minus
                        if sign_minus_flag == 1:
                            raise InvalidSignMinusError(expression[index + 1])
                        if unary_minus_flag == 1:
                            raise InvalidUnaryMinusError(expression[index + 1])
                        if (
                            expression[index + 1] != "~"
                        ):  # tilde after a minus is valid only after a binary minus
                            raise InvalidBinaryMinusError(expression[index + 1])
                else:
                    raise InvalidSingleCharError(char)

    def tilde_check(self, expression: str):
        """
        This function checks that the tildes in the expression are valid.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """

        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index].
            # tilda check
            if char == "~":
                # before tilde a value check
                if index > 0 and expression[index - 1].isdigit():
                    raise TildeAfterInvalidError(expression[index - 1])
                if index + 1 < len(expression):
                    index += 1
                    while index < len(expression) and not (
                        expression[index].isdigit() or expression[index] == "("
                    ):
                        if (
                            expression[index] in self.ops_priorities.priorities_dict
                            and expression[index] != "-"
                        ):  # check if after a tilde there is an invalid char (every operator except for minus)
                            raise TildeBeforeInvalidError(expression[index])
                        index += 1
                else:  # tilde is the last char in the expression
                    raise InvalidLastCharError(char)

    def char_placements_check(self, expression: str):
        """
        This function checks that for invalid chars placements in the expression. It checks for invalid char after parenthesis
        and for invalid char before right unary operators.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """

        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index].
            # valid char after parenthesis check
            if (
                index > 0
                and expression[index - 1] == "("
                and not (
                    char.isdigit()
                    or char == "("
                    or char == "-"
                    or char == "."
                    or self.ops_placements.get_placement(char) == "Left"
                )
            ):
                raise InvalidCharAfterParenthesisError(char)

            # valid char before right unary operator check
            if index > 0 and self.ops_placements.get_placement(char) == "Right":
                if not (
                    expression[index - 1].isdigit()
                    or expression[index - 1] == ")"
                    or self.ops_placements.get_placement(expression[index - 1])
                    == "Right"
                    or expression[index - 1] == "-"
                ):
                    raise InvalidCharBeforeRightOperatorError(
                        expression[index - 1], char
                    )

    def operators_sequence_check(self, expression: str):
        """
        This function checks for invalid operators sequences.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """

        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index].
            # 2 operators in a row ( except '-','!','#','(',')' )
            if (
                index > 0
                and self.ops_placements.get_placement(char)
                == self.ops_placements.get_placement(expression[index - 1])
                and not (
                    char.isdigit()
                    or char == "-"
                    or char == "."
                    or self.ops_placements.get_placement(char) == "Right"
                    or char == "("
                    or char == ")"
                )
            ):
                raise InvalidSequenceError(expression[index - 1], char)

    def dots_check(self, expression: str):
        """
        This function checks that the dots in the expression are valid.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """

        dot_flag = 0
        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index].
            if char == ".":
                dot_flag += 1

            # 2 dots in a row
            if dot_flag > 1:
                raise InvalidSequenceError(char, char)

            # dot before operator
            if char in self.ops_priorities.priorities_dict and dot_flag == 1:
                raise DotPlacementError(char)

            # dot after ')'
            if expression[index - 1] == ")" and dot_flag == 1:
                raise DotPlacementError(expression[index - 1])

            # dot before and after a digit
            num = char
            while index + 1 < len(expression) and char.isdigit() and dot_flag == 1:
                if expression[index + 1] == ".":
                    raise SurroundingDotsError(num)
                if expression[index + 1] in self.ops_priorities.priorities_dict:
                    dot_flag = 0
                else:
                    index += 1
                    num += expression[index]

            # dot flag resetting when a digit appears
            if char.isdigit():
                dot_flag = 0

    def parenthesis_check(self, expression: str):
        """
        This function checks that the expression parenthesis match.

        :param expression: mathematical expression in infix order
        :return: nothing if the expression is valid. else - raises an informative exception
        """

        for index, char in enumerate(
            expression
        ):  # for loop when char = expression[index]

            # parenthesis counters
            if char == "(":
                self.left_parenthesis_counter += 1
            if char == ")":
                self.right_parenthesis_counter += 1

        # equal brackets check
        if self.left_parenthesis_counter != self.right_parenthesis_counter:
            raise MismatchedParenthesesError(
                self.left_parenthesis_counter, self.right_parenthesis_counter
            )
