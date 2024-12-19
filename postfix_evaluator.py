from exceptions import MissingOperatorError, MissingOperandError
from operators import BinaryOperator, UnaryOperator
from operators_dicts import OperatorsClasses


class PostfixEvaluator:
    def __init__(self):
        pass

    def evaluate(self, postfix_list: list):
        op_classes_dict = OperatorsClasses()
        stack = []
        result = 0
        i = 0
        while i < len(postfix_list):
            char = postfix_list[i]
            if char[0] == ".":
                char = float(char)

            if op_classes_dict.get_class(char) == -1:
                stack.append(char)
            else:
                op_class = op_classes_dict.get_class(char)
                if op_class != -1:
                    if issubclass(op_class, BinaryOperator):
                        if len(stack) < 2:
                            raise MissingOperandError(char)
                        else:
                            operand2 = float(stack.pop())
                            operand1 = float(stack.pop())
                            if operand1 == float("inf") or operand2 == float("inf"):
                                raise OverflowError(
                                    "Overflow Error: Expression result is to long to be calculated"
                                )
                            result = op_class.calculate(op_class, operand1, operand2)
                            if result == float("inf"):
                                raise OverflowError(
                                    "Overflow Error: Expression result is to long to be calculated"
                                )
                            stack.append(result)
                    elif issubclass(op_class, UnaryOperator):
                        if len(stack) < 1:
                            if char == "u" or char == "s":
                                raise MissingOperandError("-")
                            else:
                                raise MissingOperandError(char)
                        else:
                            operand = float(stack.pop())
                            if operand == float("inf"):
                                raise OverflowError(
                                    "Overflow Error: Expression result is to long to be calculated"
                                )
                            result = op_class.calculate(op_class, operand)
                            if result == float("inf"):
                                raise OverflowError(
                                    "Overflow Error: Expression result is to long to be calculated"
                                )
                            stack.append(result)

            i += 1
        if len(stack) > 1:
            raise MissingOperatorError()
        return stack[-1]
