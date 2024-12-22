"""This module is the main module. This module gets the user input and returns the output (expression result or error).  """

from calculator import Calculator
from exceptions import *


def show_menu():
    # Function that displays special operators and their descriptions
    print("Special operators dictionary:")
    print("'$' - maximum (example: 3$9 = 9)")
    print("'&' - minimum (example: 3&9 = 3)")
    print("'@' - average (example: 3@9 = 6)")
    print("'~' - negative (example: ~5 = -5)")
    print("'!' - factorial (example: 4! = 1*2*3*4 = 24)")
    print("'#' - sum of digits (example: 245# = 2+4+5 = 11)")


class Main:
    calc = Calculator()
    result = 0
    exp = ""
    print(
        "Welcome the the Omega calculator! This calculator works as a regular calculator but has some special operators"
    )
    show_menu()
    while exp != "omega>sigit":  # Exit condition
        try:
            print("\nTo finish enter 'omega>sigit', to get help enter 'help me'")
            exp = input("Enter expression: ")
            if exp == "omega>sigit":
                break  # Exit the loop and calculator
            if exp == "help me":
                show_menu()  # Show the menu if the user asks for help
            else:
                result = calc.calculate(exp)
        except ZeroDivisionError as e:
            print(e)
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
        except InvalidBinaryMinusError as e:
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
        except OverflowError as e:
            print(e)
        except KeyboardInterrupt as e:
            break
        except EOFError as e:
            print("Ctrl + z pressed. to exit enter 'omega>sigit'")
        else:
            # Format the result to int if it's float with .0
            if (
                isinstance(result, float)
                and result.is_integer()
                and "e" not in str(result)
            ):
                print("Result:", int(result))
            else:
                print("Result:", result)
    print("\nexiting from calculator")
