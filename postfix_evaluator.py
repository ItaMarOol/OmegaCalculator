from exceptions import TooManyOperatorsError, NotEnoughOperatorsError
from operators_dicts import *


class PostfixEvaluator:
    def __init__(self):
        pass

    def evaluate(self, postfix_list : list):
        op_classes_dict = OperatorsClasses()
        stack = []
        result = 0
        i = 0
        while i < len(postfix_list):
            char = postfix_list[i]

            if op_classes_dict.get_class(char) == -1:
                char = float(char)
                if char.is_integer():
                    stack.append(int(char))
                else:
                    stack.append(char)
            else:
                op_class = op_classes_dict.get_class(char)
                if op_class != -1:
                    if issubclass(op_class, BinaryOperator):
                        if len(stack) < 2:
                            raise TooManyOperatorsError(char)
                        else:
                            operand2 = stack.pop()
                            operand1 = stack.pop()
                            result = op_class.calculate(op_class, operand1, operand2)
                            stack.append(result)
                    elif issubclass(op_class, UnaryOperator):
                        if len(stack) < 1:
                            if char == "u" or char == "s":
                                raise TooManyOperatorsError("-")
                            else:
                                raise TooManyOperatorsError(char)
                        else:
                            operand = stack.pop()
                            result = op_class.calculate(op_class, operand)
                            stack.append(result)

            i += 1
        if len(stack) > 1:
            raise NotEnoughOperatorsError()
        return stack[-1]



