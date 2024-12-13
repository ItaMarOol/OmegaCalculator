from exceptions import EmptyExpressionError, FirstCharError, InvalidCharError, SequenceError, DotPlacementError, \
    InvalidSingleCharError, InvalidUnaryMinusError, TildeBeforeInvalidError, TildeAfterInvalidError, \
    InvalidLastCharError, MismatchedParenthesesError
from operators_dicts import OperatorsPriority


class ValidationChecker:
    def __init__(self):
        pass

    def is_valid_expression_check(self, infix_str_expression):
        ops_dict = OperatorsPriority()
        left_parenthesis_counter = 0
        right_parenthesis_counter = 0
        dot_flag = 0
        expression = infix_str_expression.replace(" ", "")

        # empty input check
        if expression == "":
            raise EmptyExpressionError()

        char = expression[0]
        # invalid first char check
        if (
            not (
                char.isdigit()
                or char == "("
                or char == "-"
                or char == "~"
            )
        ):
            raise FirstCharError(char)

        for i in range(len(expression)):
            char = expression[i]

            # invalid char check
            if not (char.isdigit() or ops_dict.get_priority(char) != -1 or char == '(' or char == ')' or char == '.'):
                raise InvalidCharError(char)


            if char == "(":
                left_parenthesis_counter += 1
            if char == ")":
                right_parenthesis_counter += 1

            if char == ".":
                dot_flag = 1
            # 2 dots in a row
            if dot_flag > 1:
                raise SequenceError(char,char)

            # dot before operator
            if ops_dict.get_priority(char) != -1 and dot_flag == 1:
                raise DotPlacementError(char)

            # dot after operator
            if ops_dict.get_priority(expression[i - 1]) != -1 and dot_flag == 1:
                raise DotPlacementError(expression[i-1])

            # 2 operators in a row ( except '-','!','(',')' )
            if char == expression[i - 1] and not (
                char.isdigit()
                or char == "-"
                or char == "!"
                or char == "("
                or char == ")"
            ):
                raise SequenceError(char,char)

            # minus check
            if char == "-":
                if i == 0:
                    if i + 1 < len(expression):
                        while i + 1 < len(expression) and expression[i+1] == "-":
                            i += 1
                        if not (
                                expression[i + 1].isdigit() or  expression[i + 1] == "-" or  expression[i + 1] == "("
                        ):
                            raise InvalidUnaryMinusError(expression[i+1])
                    else:
                        raise InvalidSingleCharError(char)

            # tilda check
            if char == "~":
                # before tilde a value check
                if i > 0 and expression[i-1].isdigit():
                    raise TildeBeforeInvalidError(expression[i-1])
                if i + 1 < len(expression):
                    next_char = expression[i + 1]
                    if not (
                        next_char.isdigit() or next_char == "-" or next_char == "("
                    ):
                        raise TildeAfterInvalidError(next_char)
                else:
                    raise InvalidLastCharError(char)
            if ops_dict.get_priority(char) != -1:
                dot_flag = 0

        # last char is digit/'!')'
        if not (
            expression[-1].isdigit()
            or expression[-1] == "!"
            or expression[-1] == ")"
        ):
            raise InvalidLastCharError(expression[-1])

        # equal brackets check
        if left_parenthesis_counter != right_parenthesis_counter:
            raise MismatchedParenthesesError(left_parenthesis_counter, right_parenthesis_counter)
        return True


