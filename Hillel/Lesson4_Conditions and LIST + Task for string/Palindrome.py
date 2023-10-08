user_input = input("Enter word or phrase: ")

cleaned_input = user_input.replace(" ", "").lower()

reversed_input = cleaned_input[::-1]

if cleaned_input == reversed_input:
    print("This is Palindrome")
else:
    print("This is not Palindrome, try again")
