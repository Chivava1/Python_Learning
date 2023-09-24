#Calculate the number of apples divided by the number of students
num_appl = int(input(" Input Amount of Apples: "))
num_pup = int(input("Input Number of pupils: "))
result = num_appl // num_pup
result1 = num_appl % num_pup

print("Apples per pupil", result)
print("Left in bin", result1)