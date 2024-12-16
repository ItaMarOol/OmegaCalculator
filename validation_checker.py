from exceptions import EmptyExpressionError, FirstCharError, InvalidCharError, SequenceError, DotPlacementError, \
    InvalidSingleCharError, InvalidUnaryMinusError, TildeBeforeInvalidError, TildeAfterInvalidError, \
    InvalidLastCharError, MismatchedParenthesesError, SurroundingDotsError, InvalidSignMinusError, InvalidMinusError, \
    InvalidCharAfterParenthesisError, InvalidCharBeforeRightOperatorError
from operators_dicts import OperatorsPriorities, OperatorsPlacements


class ValidationChecker:
    def __init__(self):
        pass

    def is_valid_expression_check(self, infix_str_expression : str):

        ops_priorities = OperatorsPriorities()
        ops_placements = OperatorsPlacements()
        left_parenthesis_counter = 0
        right_parenthesis_counter = 0
        dot_flag = 0

        # removing white spaces
        expression = infix_str_expression.replace(" ", "").replace("\t","")

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
                or char == "."
            )
        ):
            raise FirstCharError(char)

        # Invalid last char check
        if not (
            expression[-1].isdigit()
            or ops_placements.get_placement(expression[-1]) == "Right"
            or expression[-1] == ")"
        ):
            raise InvalidLastCharError(expression[-1])

        for index in range(len(expression)):
            char = expression[index]
            sign_minus_flag = 0
            unary_minus_flag = 0
            minus_flag = 0

            # invalid char check
            if not (char.isdigit() or ops_priorities.get_priority(char) != -1 or char == "(" or char == ")" or char == "."):
                raise InvalidCharError(char)


            if char == "(":
                left_parenthesis_counter += 1
            if char == ")":
                right_parenthesis_counter += 1

            if char == ".":
                dot_flag += 1
            # 2 dots in a row
            if dot_flag > 1:
                raise SequenceError(char,char)

            # dot before operator
            if ops_priorities.get_priority(char) != -1 and dot_flag == 1:
                raise DotPlacementError(char)

            # dot after ')'
            if expression[index-1] == ")" and dot_flag == 1:
                raise DotPlacementError(expression[index-1])

            # dot before and after a digit
            num = char
            while index + 1 < len(expression) and char.isdigit() and dot_flag == 1 :
                if expression[index+1] == ".":
                    raise SurroundingDotsError(num)
                elif ops_priorities.get_priority(expression[index+1]) != -1:
                    dot_flag = 0
                else:
                    index += 1
                    num += expression[index]

            # 2 operators in a row ( except '-','!','#','(',')' )
            if index > 0 and ops_placements.get_placement(char) == ops_placements.get_placement(expression[index-1]) and not (
                char.isdigit()
                or char == "-"
                or char == "."
                or ops_placements.get_placement(char) == "Right"
                or char == "("
                or char == ")"
            ):
                raise SequenceError(expression[index-1],char)

            # minus check
            if char == "-":
                if index == 0 or expression[index-1] == "(":
                    unary_minus_flag = 1
                elif expression[index-1].isdigit() or expression[index-1] == ")":
                    minus_flag = 1
                elif ops_priorities.get_priority(expression[index-1]) != -1:
                    sign_minus_flag = 1

                if index + 1 < len(expression):
                    while index + 1 < len(expression) and expression[index+1] == "-":
                        index += 1
                        sign_minus_flag = 1
                    if not (
                            expression[index + 1].isdigit() or  expression[index + 1] == "-" or  expression[index + 1] == "("
                    ):
                        if sign_minus_flag == 1:
                            raise InvalidSignMinusError(expression[index+1])
                        elif unary_minus_flag == 1:
                            raise InvalidUnaryMinusError(expression[index+1])
                        else:
                            raise InvalidMinusError(expression[index+1])
                else:
                    raise InvalidSingleCharError(char)

            # tilda check
            if char == "~":
                # before tilde a value check
                if index > 0 and expression[index-1].isdigit():
                    raise TildeAfterInvalidError(expression[index-1])
                if index + 1 < len(expression):
                    index += 1
                    while index < len(expression) and not (expression[index].isdigit() or expression[index] == "("):
                        if ops_priorities.get_priority(expression[index]) != -1 and expression[index] != "-":
                            raise TildeBeforeInvalidError(expression[index])
                        index += 1
                else:
                    raise InvalidLastCharError(char)
            if char.isdigit():
                dot_flag = 0
            if index > 0 and expression[index-1] == "(" and not(char.isdigit() or char == "-" or char == "." or ops_placements.get_placement(char) == "Left"):
                raise InvalidCharAfterParenthesisError(char)
            if index > 0 and ops_placements.get_placement(char) == "Right":
                if not (expression[index-1].isdigit() or expression[index-1] == ")" or ops_placements.get_placement(expression[index-1]) == "Right" or expression[index-1] == "-"):
                    raise InvalidCharBeforeRightOperatorError(expression[index-1], char)
        # equal brackets check
        if left_parenthesis_counter != right_parenthesis_counter:
            raise MismatchedParenthesesError(left_parenthesis_counter, right_parenthesis_counter)
        return True


