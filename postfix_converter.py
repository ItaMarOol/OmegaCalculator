from minus_manager import MinusManager
from operators_dicts import OperatorsPriorities, OperatorsPlacements


class InfixToPostfixConverter:
    def __init__(self):
        pass

    def to_postfix(self, expression: list) -> list:
        postfix_output = []
        stack = []
        ops_priorities = OperatorsPriorities()
        ops_placements = OperatorsPlacements()

        index = 0
        while index < len(expression):
            char = expression[index]

            if char.isdigit() or char.lstrip("-").isdigit() or char == ".":
                number = char
                while index + 1 < len(expression) and (expression[index + 1].isdigit() or expression[index + 1] == '.'):
                    index += 1
                    number += expression[index]
                postfix_output.append(number)

            elif char == "(":
                stack.append(char)

            elif char == ")":
                while stack and stack[-1] != "(":
                    postfix_output.append(stack.pop())
                stack.pop()

            else:
                while (stack and stack[-1] != "(" and
                       (ops_priorities.get_priority(stack[-1]) > ops_priorities.get_priority(char) or (ops_priorities.get_priority(stack[-1]) == ops_priorities.get_priority(char) and char != "s" and char != "u")
                               )):
                    postfix_output.append(stack.pop())
                else:
                    if ops_placements.get_placement(char) == "Right":
                        postfix_output.append(char)
                    else:
                        stack.append(char)

            index += 1

        while stack:
            postfix_output.append(stack.pop())

        return postfix_output
