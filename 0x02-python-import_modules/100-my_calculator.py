#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv)
    if n - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] == "+":
        addition = add(int(sys.argv[1]), int(sys.argv[3]))
        print(sys.argv[1] + " + " + sys.argv[3] + " = " + str(addition))
    elif sys.argv[2] == "-":
        subtraction = sub(int(sys.argv[1]), int(sys.argv[3]))
        print(sys.argv[1] + " - " + sys.argv[3] + " = " + str(subtraction))
    elif sys.argv[2] == "*":
        multiplication = mul(int(sys.argv[1]), int(sys.argv[3]))
        print(sys.argv[1] + " * " + sys.argv[3] + " = " + str(multiplication))
    elif sys.argv[2] == "/":
        division = div(int(sys.argv[1]), int(sys.argv[3]))
        print(sys.argv[1] + " / " + sys.argv[3] + " = " + str(division))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
