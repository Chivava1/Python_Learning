course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

key = input("Input key: ")

try:
    value = course[key]
    print(f"Value for key '{key}': {value}")
except KeyError:
    print(f"Key '{key}' wasn't found.")