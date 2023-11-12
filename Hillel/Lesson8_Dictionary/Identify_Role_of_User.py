roles = {
    'admin': ['Alice', 'Bob', 'Charlie'],
    'maintainer': ['David', 'Eve'],
    'manager': ['Frank', 'Grace'],
    'developer': ['Hank', 'Ivy']
}

user_name = input("Input username: ")

user_role = None
for role, user_list in roles.items():
    if user_name in user_list:
        user_role = role
        break

if user_role:
    print(f"Hello, {user_role}")
else:
    print("Hello, Guest")