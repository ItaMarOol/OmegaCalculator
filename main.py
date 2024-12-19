from calculator import Calculator
from exceptions import  *


def showMenu():
    print("Special operators dictionary:")
    print("'$' - maximum (example: 3$9 = 9)")
    print("'&' - minimum (example: 3$9 = 3)")
    print("'@' - average (example: 3$9 = 6)")
    print("'~' - negative (example: ~5 = -5)")
    print("'!' - factorial (example: 4! = 1*2*3*4 = 24)")
    print("'#' - sum of digits (example: 245# = 2+4+5 = 11)")


class Main:
    calc = Calculator()
    exp = ""
    print(
        "Welcome the the Omega calculator! This calculator works as a regular calculator but has some special operators"
    )
    showMenu()
    while exp != "omega>sigit":
        print("\nTo finish enter 'omega>sigit', to get help enter 'help me'")
        exp = input("Enter expression: ")
        if exp == "omega>sigit":
            break
        if exp == "help me":
            showMenu()
        else:
            try:
                result = calc.calculate(exp)
            except FactorialArgumentError as e:
                print(e)
            except HashtagArgumentError as e:
                print(e)
            except PowerByFractionError as e:
                print(e)
            except ZeroPowerError as e:
                print(e)
            except MissingOperandError as e:
                print(e)
            except MissingOperatorError as e:
                print(e)
            except InvalidFirstCharError as e:
                print(e)
            except EmptyExpressionError as e:
                print(e)
            except InvalidSequenceError as e:
                print(e)
            except DotPlacementError as e:
                print(e)
            except SurroundingDotsError as e:
                print(e)
            except InvalidCharError as e:
                print(e)
            except InvalidUnaryMinusError as e:
                print(e)
            except InvalidMinusError as e:
                print(e)
            except InvalidSignMinusError as e:
                print(e)
            except TildeAfterInvalidError as e:
                print(e)
            except TildeBeforeInvalidError as e:
                print(e)
            except InvalidSingleCharError as e:
                print(e)
            except InvalidLastCharError as e:
                print(e)
            except MismatchedParenthesesError as e:
                print(e)
            except InvalidCharAfterParenthesisError as e:
                print(e)
            except InvalidCharBeforeRightOperatorError as e:
                print(e)
            else:
                if isinstance(result, float) and result.is_integer() and "e" not in str(result):
                    print("Result:", int(result))
                else:
                    print("Result:", result)
    print("exited from calculator")
