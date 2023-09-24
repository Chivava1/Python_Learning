input_string = input("Enter word/phrase to modify: ")

letter_to_remove = input("Enter spell should be deleted: ")

modified_string = input_string.replace(letter_to_remove, '')

print(f"Modified String: {modified_string}")