"""This module handling the evaluation of a postfix expression."""
from exceptions import MissingOperatorError, MissingOperandError
from operators import BinaryOperator, UnaryOperator
from operators_dicts import OperatorsClasses


class PostfixEvaluator:
    """This class evaluates a postfix expression."""

    def __init__(self):
        pass

    def evaluate(self, postfix_list: list):
        """
        This function evaluates a postfix expression.

        :param postfix_list: list with mathematical expression in postfix order
        :return: the mathematical expression result
        """
        ops_classes = OperatorsClasses()
        stack = []
        result = 0
        i = 0
        while i < len(postfix_list):
            char = postfix_list[i]

            if char not in ops_classes.classes_dict:  # check if is a value
                stack.append(char)
            else:
                op_class = ops_classes.get_class(char)
                if op_class != -1:  # check if it is a valid operator
                    if issubclass(op_class, BinaryOperator):
                        if len(stack) < 2:
                            raise MissingOperandError(char)

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
                            if char in ("u","s"):
                                raise MissingOperandError("-")
                            raise MissingOperandError(char)

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
        return float(stack[-1])
