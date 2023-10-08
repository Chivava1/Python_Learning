input_numbers = input(f"Input numbers, use space as separator: ").split()
print(input_numbers)

if len(input_numbers) == len(set(input_numbers)):
    print("All numbers are unique.")
else:
    print("There are duplicates in list.")

