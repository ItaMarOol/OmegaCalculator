import pytest
from calculator import Calculator
from exceptions import *

calculator = Calculator()

def test_invalid_factorial_expression():
    with pytest.raises(FactorialArgumentError):
        calculator.calculate("2--3!")

def test_invalid_operators_sequence_expression():
    with pytest.raises(InvalidSequenceError):
        calculator.calculate("4+*5")

def test_mismatched_parentheses_expression():
    with pytest.raises(MismatchedParenthesesError):
        calculator.calculate("(9+(2)")

def test_divide_by_zero_expression():
    with pytest.raises(ZeroDivisionError):
        calculator.calculate("5/0")

def test_missing_operator_expression():
    with pytest.raises(MissingOperatorError):
        calculator.calculate("4(~5)")

def test_empty_expression():
    with pytest.raises(EmptyExpressionError):
        calculator.calculate("")

def test_white_spaces_expression():
    with pytest.raises(EmptyExpressionError):
        calculator.calculate("               ")

def test_gibberish_expression():
    with pytest.raises(InvalidFirstCharError):
        calculator.calculate(";owieht0v-2976")
    with pytest.raises(InvalidLastCharError):
        calculator.calculate("09n32pv7ywvetpm   2t]")
    with pytest.raises(InvalidCharError):
        calculator.calculate("0;sligdhmv;aowijoptwa6")

def test_simple_addition_expression():
    assert calculator.calculate("3+8") == 11

def test_simple_subtraction_expression():
    assert calculator.calculate("7-5") == 2

def test_simple_multiplication_expression():
    assert calculator.calculate("5*7") == 35

def test_simple_division_expression():
    assert calculator.calculate("15/2") == 7.5

def test_simple_power_expression():
    assert calculator.calculate("3^3") == 27

def test_simple_modulo_expression():
    assert calculator.calculate("8%3") == 2

def test_simple_maximum_expression():
    assert calculator.calculate("15$9") == 15

def test_simple_minimum_expression():
    assert calculator.calculate("15&9") == 9

def test_simple_average_expression():
    assert calculator.calculate("10@2") == 6

def test_simple_tilde_expression():
    assert calculator.calculate("~11") == -11

def test_simple_factorial_expression():
    assert calculator.calculate("5!") == 120

def test_simple_hashtag_expression():
    assert calculator.calculate("134#") == 8

def test_simple_addition_multiplication_expression():
    assert calculator.calculate("4 + 6 * 2") == 16

def test_complex_minus_expression():
    assert calculator.calculate("~ - - - ( - - 2 ) - - 4") == 6

def test_complex_expression1():
    assert calculator.calculate("3 ! - ~ - 10 ^ 2 @ 4 * 2 + ~ 4 & 9 - 2") == -2000

def test_complex_expression2():
    assert calculator.calculate("(10 + 4 * 3) $ (7 - 5) & ((2 ^ 3) + 4) * (6 % 4) - 10") == 14

def test_complex_expression3():
    assert calculator.calculate("5 + 2 * (3^2) - (6 + 4) % 3 * 7 / (4 - 2) @ 5") == 21

def test_complex_expression4():
    assert calculator.calculate("(6 + 2 * 3) ^ 2 / 1 @ 1.88") == 100

def test_complex_expression5():
    assert calculator.calculate("( ( ( 5 * 2 ) ^ 2 - - 8 ) + 9 $ 21 ) #") == 12

def test_complex_expression6():
    assert calculator.calculate("5 * (8 + 3^2) - 10 % 3 + 12 @ 6 * 7 - (15 & 10) + (4 $ 9) - 7!") == -4894

def test_complex_expression7():
    assert calculator.calculate("(7 * 2 + 4) @ 6 + (9 / 3) - (14 % 5) + 3 ^ 3") == 38

def test_complex_expression8():
    assert calculator.calculate("3 ^ 2 + (5 ! / 10) @ 4") == 17

def test_complex_expression9():
    assert calculator.calculate("5 ! - - 3 ^ 3 + 2 * 4 - - 8 @ 6") == 156

def test_complex_expression10():
    assert calculator.calculate("(4 ^ 2 - 5) * (3 @ 7) - 6 ! + (12 # )") == -662

def test_complex_expression11():
    assert calculator.calculate("4 ! - - (10 * 2) + (6 & 4) - (4 @ 3)") == 44.5

def test_complex_expression12():
    assert calculator.calculate("5 * 3 - (2 ^ 4) + 7 @ (6 * 2) - 9 % 4 + 41 #") == 12.5

def test_complex_expression13():
    assert calculator.calculate("((6 + 2) * (4 - 1)) - (4 ^ (2 + 1)) + (8 & 3) @ 2") == -37.5

def test_complex_expression14():
    assert calculator.calculate("3 + 2 * 5 ^ (0 + 3) - 6 @ (6 - 2) + (8 % 3) + (5 & (3 + 2))") == 255

def test_complex_expression15():
    assert calculator.calculate("2.5 + (2 * (5 ^ 2)) - (6 @ (4 - 1))") == 48

def test_complex_expression16():
    assert calculator.calculate("( ( 6 + (5 * 2)) ^ 2 - (8 & 3) ) #") == 10