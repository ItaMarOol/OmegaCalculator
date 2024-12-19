from calculator import Calculator


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
            except Exception as e:
                print(str(e))
            else:
                if isinstance(result, float) and result.is_integer() and "e" not in str(result):
                    print("Result:", int(result))
                else:
                    print("Result:", result)
    print("exited from calculator")
