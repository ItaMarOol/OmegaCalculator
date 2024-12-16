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
            result = calc.calculate(exp)
            if isinstance(result, int) or isinstance(result, float):
                print("Result:", result)
            else:
                print(result)
    print("exited from calculator")
