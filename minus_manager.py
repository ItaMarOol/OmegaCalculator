from operators_dicts import *


class MinusManager:
    def __init__(self):
        pass

    def manage(self, infix_expression: str) -> list:
        ops_priorities = OperatorsPriorities()
        ops_placements = OperatorsPlacements()
        output = []
        index = 0

        # removing white spaces
        infix_expression = infix_expression.replace(" ", "").replace("\t", "")

        while index < len(infix_expression):
            # unary minus check
            if infix_expression[index] == "-" and (
                index == 0 or infix_expression[index - 1] == "("
            ):
                while index < len(infix_expression) and infix_expression[index] == "-":
                    output.append("u")
                    index += 1
            # binary minus check
            elif (
                infix_expression[index] == "-"
                and index > 0
                and (
                    infix_expression[index - 1].isdigit()
                    or ops_placements.get_placement(infix_expression[index - 1])
                    == "Right"
                    or infix_expression[index - 1] == ")"
                )
            ):
                output.append("-")
                index += 1
                # sign minus check
                while index < len(infix_expression) and infix_expression[index] == "-":
                    output.append("s")
                    index += 1
            # sign minus check
            elif (
                infix_expression[index] == "-"
                and index > 0
                and ops_priorities.get_priority(infix_expression[index - 1]) != -1
            ):
                while index < len(infix_expression) and infix_expression[index] == "-":
                    output.append("s")
                    index += 1
            else:
                output.append(infix_expression[index])
                index += 1
        return output
