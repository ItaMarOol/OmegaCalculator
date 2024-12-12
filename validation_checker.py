from operators_dicts import *


class ValidationChecker:
    def __init__(self):
        pass

    def is_valid_expression_check(self, infix_str_expression):
        ops_dict = OperatorsPriority()
        left_bracket_counter = 0
        right_bracket_counter = 0
        dot_flag = 0
        expression = infix_str_expression.replace(" ", "")

        # empty input check
        if expression == "":
            return False

        char = expression[0]
        # invalid first char check
        if (
            not (
                char.isdigit()
                or char == "("
                or char == "+"
                or char == "-"
                or char == "~"
            )
        ):
            return False

        for i in range(len(expression)):
            char = expression[i]

            if char == "(":
                left_bracket_counter += 1
            if char == ")":
                right_bracket_counter += 1

            if char == ".":
                dot_flag = 1
            # 2 dots in a row
            if dot_flag > 1:
                return False
            # dot before operator
            if ops_dict.get_priority(char) != -1 and dot_flag == 1:
                return False
            # dot after operator
            if ops_dict.get_priority(expression[i - 1]) != -1 and dot_flag == 1:
                return False
            # 2 operators in a row ( except '-','!','(',')' )
            if char == expression[i - 1] and not (
                char.isdigit()
                or char == "-"
                or char == "!"
                or char == "("
                or char == ")"
            ):
                return False

            # minus check
            if char == "-":
                if i == 0:
                    if i + 1 < len(expression):
                        while i + 1 < len(expression) and expression[i+1] == "-":
                            i += 1
                        if not (
                                expression[i + 1].isdigit() or  expression[i + 1] == "-" or  expression[i + 1] == "("
                        ):
                            return False
                    else:
                        return False
                #elif (ops_dict.get_priority(expression[i - 1]) != -1):

            # tilda check
            if char == "~":
                if i + 1 < len(expression):
                    next_char = expression[i + 1]
                    if not (
                        next_char.isdigit() or next_char == "-" or next_char == "("
                    ):
                        return False
                else:
                    return False
            if ops_dict.get_priority(char) != -1:
                dot_flag = 0

        # last char is digit
        if not (
            expression[-1].isdigit()
            or expression[-1] == "!"
            or expression[-1] == "#"
            or expression[-1] == ")"
        ):
            return False

        # equal brackets check
        if left_bracket_counter != right_bracket_counter:
            return False
        return True


