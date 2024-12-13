from exceptions import *
from postfix_converter import InfixToPostfixConverter
from postfix_evaluator import PostfixEvaluator
from validation_checker import ValidationChecker


class Calculator:
    def __init__(self):
        self.valid_checker = ValidationChecker()
        self.postfix_converter = InfixToPostfixConverter()
        self.postfix_calculator = PostfixEvaluator()

    def calculate(self, expression):
        try:
            self.valid_checker.is_valid_expression_check(expression)
        except FirstCharError as e:
            return e.__str__()
        except EmptyExpressionError as e:
            return e.__str__()
        except SequenceError as e:
            return e.__str__()
        except DotPlacementError as e:
            return e.__str__()
        except InvalidCharError as e:
            return e.__str__()
        except InvalidUnaryMinusError as e:
            return e.__str__()
        except TildeAfterInvalidError as e:
            return e.__str__()
        except TildeBeforeInvalidError as e:
            return e.__str__()
        except InvalidSingleCharError as e:
            return e.__str__()
        except InvalidLastCharError as e:
            return e.__str__()
        except MismatchedParenthesesError as e:
            return e.__str__()

        else:
            postfix_expression = self.postfix_converter.to_postfix(expression)
            try:
                result = self.postfix_calculator.evaluate(postfix_expression)
            except FactorialArgumentError as e:
                return e.__str__()
            except ZeroDivisionError as e:
                return e.__str__()
            except PowerArgumentError as e:
                return e.__str__()
            except TooManyOperatorsError as e:
                return e.__str__()
            except NotEnoughOperatorsError as e:
                return e.__str__()
            else:
                return result