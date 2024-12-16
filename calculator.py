from minus_manager import MinusManager
from postfix_converter import InfixToPostfixConverter
from postfix_evaluator import PostfixEvaluator
from validation_checker import ValidationChecker


class Calculator:
    def __init__(self):
        self.valid_checker = ValidationChecker()
        self.minusManager = MinusManager()
        self.postfix_converter = InfixToPostfixConverter()
        self.postfix_calculator = PostfixEvaluator()

    def calculate(self, expression):
        try:
            self.valid_checker.is_valid_expression_check(expression)
        except Exception as e:
            return str(e)

        else:
            expression = self.minusManager.manage(expression)
            postfix_expression = self.postfix_converter.to_postfix(expression)
            try:
                result = self.postfix_calculator.evaluate(postfix_expression)
            except Exception as e:
                return str(e)
            else:
                return result
