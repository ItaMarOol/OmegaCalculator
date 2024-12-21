"""This module manages the expression minuses. """

from operators_dicts import OperatorsPriorities, OperatorsPlacements


class MinusManager:
    """This class responsible for managing the expression minuses and inserting the right minuses in each place. """
    def __init__(self):
        pass

    def manage(self, infix_expression: str) -> list:
        """
        This function replaces every minus in the expression with the correct minus (binary/unary/sign)

        :param infix_expression: mathematical expression in infix order
        :return: the expression with the right minuses marked by operators ("u" for unary minus, "s" for sign minus)
        """
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
                # minus sequence check
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
                # minus sequence check
                while index < len(infix_expression) and infix_expression[index] == "-":
                    output.append("s")
                    index += 1
            # sign minus check
            elif (
                infix_expression[index] == "-"
                and index > 0
                and infix_expression[index - 1] in ops_priorities.priorities_dict
            ):
                # minus sequence check
                while index < len(infix_expression) and infix_expression[index] == "-":
                    output.append("s")
                    index += 1
            else:  # not a minus
                output.append(infix_expression[index])
                index += 1
        return output
