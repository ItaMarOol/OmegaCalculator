from calculator import Calculator

calc = Calculator()
exp = ""
while exp != "omega>sigit":
    exp = input("Enter expression (to finish enter 'omega>sigit'): ")
    if exp == "omega>sigit":
        break
    else:
        result = calc.calculate(exp)
        if isinstance(result, int) or isinstance(result, float):
            print("Result:" ,result)
        else:
            print(result)
print("exited from calculator")