user_input = int(input("Enter a number of Petals: "))
list_of_phrases = ["A little", "A lot", "Passionately", "Madly", "Not at all", "I love you"]

if user_input <= len(list_of_phrases):
    print(f"The last petal is:", list_of_phrases[user_input - 1])
else:
    exceeded_list = user_input % len(list_of_phrases)
    print(f"The last petal is:", list_of_phrases[exceeded_list - 1])








