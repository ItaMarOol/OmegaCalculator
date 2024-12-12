from abc import ABC, abstractmethod

class BinaryOperator(ABC):
    def __init__(self, operator):
        self.operator = operator
    @abstractmethod
    def calculate(self, operand1, operand2):
        ...

class UnaryOperator(ABC):
    def __init__(self, operator):
        self.operator = operator
    @abstractmethod
    def calculate(self, operand):
        ...






class Addition(BinaryOperator):
    def calculate(self, operand1, operand2):
        return operand1 + operand2

class Subtraction(BinaryOperator):
    def calculate(self, operand1, operand2):
        return operand1 - operand2

class Multiplication(BinaryOperator):
    def calculate(self, operand1, operand2):
        return operand1 * operand2

class Division(BinaryOperator):
    def calculate(self, operand1, operand2):
        if (operand2 == 0):
            raise ZeroDivisionError("Can't divide by zero")
        return float(operand1) / operand2


class Power(BinaryOperator):
    def calculate(self, operand1, operand2):
        return pow(operand1, operand2)


class Modulo(BinaryOperator):
    def calculate(self, operand1, operand2):
        if operand2 == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return operand1 % operand2


class Maximum(BinaryOperator):
    def calculate(self, operand1, operand2):
        if (operand1 > operand2):
            return operand1
        return operand2


class Minimum(BinaryOperator):
    def calculate(self, operand1, operand2):
        if (operand1 < operand2):
            return operand1
        return operand2


class Average(BinaryOperator):
    def calculate(self, operand1, operand2):
        return float(operand1+operand2)/2

class UnaryMinus(UnaryOperator):
    def calculate(self, operand):
        return -1 * operand

class Tilde(UnaryOperator):
    def calculate(self, operand):
        return -1 * operand


class Factorial(UnaryOperator):
    def calculate(self, operand):
        factorial_sum = 1
        if not isinstance(operand, int) and operand.is_integer():
            operand = int(operand)
        if not isinstance(operand, int) or operand < 0:
            # raise FactorialArgumentError(operand)
            ...
        else:
            for i in range(1, operand + 1):
                factorial_sum *= i
        return factorial_sum



