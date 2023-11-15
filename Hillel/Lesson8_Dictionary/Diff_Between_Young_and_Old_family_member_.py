family = {
    'grandpa': ('Alex', 76),
    'grandma': ('Nona', 74),
    'dad': ('Greg', 48),
    'mom': ('July', 45),
    'son_older': ('Bob', 18),
    'son_middle': ('Alex', 15),
    'son_young': ('Mark', 10)
}

ages = [age for name, (name, age) in family.items()]
max_age = max(ages)
min_age = min(ages)
difference = max_age - min_age
print(f"The difference between the oldest and youngest family member's ages is {difference} years.")