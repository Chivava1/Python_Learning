print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplying")
print("4. Division")

choice = input("Choose Operation Code (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    option = "+"
elif choice == "2":
    result = num1 - num2
    option = "-"
elif choice == "3":
    result = num1 * num2
    option = "*"
elif choice == "4":
    if num2 == 0:
        print("Division on 0 is forbidden")
    else:
        result = num1 / num2
        option = "/"

else:
    print("Invalid operation")

print(f"Result: {num1} {option} {num2} = {result}")
