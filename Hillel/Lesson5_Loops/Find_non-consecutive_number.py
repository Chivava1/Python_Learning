#Write a program to find the first consecutive number in a list
lst = input("Enter list of numbers, use Space as separator: ").split()
lst = [int(item) for item in lst]

for n in range(1, len(lst)):
    current_item = lst[n]
    previous_item = lst[n - 1]
    if current_item != previous_item + 1:
        print("First non-consecutive number is:", current_item)
        break
    else:
        print("All list consists from consecutive numbers.")

