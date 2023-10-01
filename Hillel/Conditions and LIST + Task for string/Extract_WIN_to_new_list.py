my_list = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]

win_extraction = my_list[6][3][0]

print(f"Congratulations!, ", {win_extraction}, " has been extracted")