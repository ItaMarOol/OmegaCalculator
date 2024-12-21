"""This module controls and manages the calculator """
from minus_manager import MinusManager
from postfix_converter import InfixToPostfixConverter
from postfix_evaluator import PostfixEvaluator
from validation_checker import ValidationChecker


class Calculator:
    """This class includes all the calculator processes"""

    def __init__(self):
        self.valid_checker = ValidationChecker()
        self.minus_manager = MinusManager()
        self.postfix_converter = InfixToPostfixConverter()
        self.postfix_calculator = PostfixEvaluator()

    def calculate(self, expression: str):
        """
        This function calculates a mathematical expression.

        :param expression: mathematical expression
        :return: the mathematical expression result
        """
        self.valid_checker.is_valid_expression_check(expression)
        expression = self.minus_manager.manage(expression)
        postfix_expression = self.postfix_converter.to_postfix(expression)
        result = self.postfix_calculator.evaluate(postfix_expression)
        return result
