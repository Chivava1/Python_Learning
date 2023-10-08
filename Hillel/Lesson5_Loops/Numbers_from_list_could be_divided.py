#Write a program to print all the numbers in the list that fall on a given number. Set the number from the keyboard.                                     #
numbers = input("Enter numbers, use Space as separator: ").split()
divider = int(input("Enter number, at which should be deleted: "))

print(f"List of numbers could be deleted on {divider}",":")
for i in numbers:
    if int(i) % divider == 0:
        print(i)