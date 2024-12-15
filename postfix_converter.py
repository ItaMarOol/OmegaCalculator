from minus_manager import MinusManager
from operators_dicts import OperatorsPriorities, OperatorsPlacements


class InfixToPostfixConverter:
    def __init__(self):
        pass

    def to_postfix(self, str_expression):
        postfix_output = []
        stack = []
        ops_priorities = OperatorsPriorities()
        ops_placements = OperatorsPlacements()
        minus_manager = MinusManager()
        expression = minus_manager.manage(str_expression)

        i = 0
        while i < len(expression):
            char = expression[i]

            if char.isdigit() or char.lstrip("-").isdigit() or char == ".":
                number = char
                while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                    i += 1
                    number += expression[i]
                postfix_output.append(number)

            elif char == "(":
                stack.append(char)

            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix_output.append(stack.pop())
                stack.pop()

            else:
                while (stack and stack[-1] != "(" and
                       (ops_priorities.get_priority(stack[-1]) > ops_priorities.get_priority(char) or (ops_priorities.get_priority(stack[-1]) == ops_priorities.get_priority(char) and char != "s")
                               )):
                    postfix_output.append(stack.pop())
                else:
                    if ops_placements.get_placement(char) == "Right":
                        postfix_output.append(char)
                    else:
                        stack.append(char)

            i += 1

        while stack:
            postfix_output.append(stack.pop())

        return postfix_output
