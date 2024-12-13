from operators_dicts import *


class MinusManager:
    def __init__(self):
        pass

    def manage(self, infix_expression):
        ops_dict = OperatorsPriority()
        output = []
        i = 0
        starting_minus_counter = 0
        minus_counter = 0

        # removing white spaces
        infix_expression = infix_expression.replace(" ", "").replace("\t","")

        # first unary minuses check
        if len(infix_expression) > 1 and infix_expression[0] == "-":
            while i < len(infix_expression) and infix_expression[i] == "-":
                starting_minus_counter += 1
                i += 1
            if starting_minus_counter % 2 == 1:
                output.append("u")
        while i < len(infix_expression):
            # minuses sequence check
            if i > 0 and infix_expression[i] == "-" and infix_expression[i - 1] == "-":
                while infix_expression[i] == "-":
                    minus_counter += 1
                    i += 1
                if minus_counter % 2 == 0:
                    output.append(infix_expression[i])
                else:
                    # after minuses sequence is operator check
                    if ops_dict.get_priority(infix_expression[i]) != -1:
                        output.pop()  # popping inserted minus
                        output.append("+")
                        output.append(infix_expression[i])
                    else: # minus sign attached to a value
                        output.append(
                            "-" + infix_expression[i]
                        )
                i += 1
            # minus after operator (except '!', '(' )
            elif (
                i > 0
                and infix_expression[i] == "-"
                and (
                    ops_dict.get_priority(infix_expression[i - 1]) != -1
                    and infix_expression[i - 1] != "!"
                    or infix_expression[i - 1] == "("
                )
            ):
                while infix_expression[i] == "-":
                    minus_counter += 1
                    i += 1
                if minus_counter % 2 == 0:
                    temp = ""
                    while i < len(infix_expression) and infix_expression[i].isdigit():
                        temp += infix_expression[i]
                        i += 1
                    output.append(temp)
                else:
                    temp = "-"
                    while i < len(infix_expression) and infix_expression[i].isdigit():
                        temp += infix_expression[i]
                        i += 1
                    output.append(temp)
            else:
                output.append(infix_expression[i])
                i += 1
            minus_counter = 0
        return output

