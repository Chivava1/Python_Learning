def calculator(num1: float, num2: float, choice: str):
    result = None
    if choice == "+":
        result = num1 + num2
    elif choice == "-":
        result = num1 - num2
    elif choice == "*":
        result = num1 * num2
    elif choice == "/":
        if num2 == 0:
            print("Division on 0 is forbidden")
        else:
            result = num1 / num2

    else:
        print("Invalid operation")

    if result is not None:
        print(f"Result: {num1} {choice} {num2} = {result}")


calculator(3, 0, "/")
