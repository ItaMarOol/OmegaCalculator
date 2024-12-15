from operators_dicts import *


class MinusManager:
    def __init__(self):
        pass

    def manage(self, infix_expression):
        ops_priorities = OperatorsPriorities()
        output = []
        i = 0

        # removing white spaces
        infix_expression = infix_expression.replace(" ", "").replace("\t","")

        while i < len(infix_expression):
            # unary minus check
            if infix_expression[i] == "-" and (i == 0 or infix_expression[i - 1] == "("):
                    output.append("u")
                    i += 1
                    # sign minus check
                    while i < len(infix_expression) and infix_expression[i] == "-":
                        output.append("u")
                        i += 1
            # binary minus check
            elif infix_expression[i] == "-" and i > 0 and (infix_expression[i-1].isdigit() or infix_expression[i-1] == ")"):
                    output.append("-")
                    i += 1
                    # sign minus check
                    while i < len(infix_expression) and infix_expression[i] == "-":
                        output.append("s")
                        i += 1
            # sign minus check
            elif infix_expression[i] == "-" and i > 0 and ops_priorities.get_priority(infix_expression[i-1] != -1):
                while i < len(infix_expression) and infix_expression[i] == "-":
                    output.append("s")
                    i+=1
            else:
                output.append(infix_expression[i])
                i += 1
        return output

