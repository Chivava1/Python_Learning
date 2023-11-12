with open('Initial_text_file.txt', 'r', encoding='utf8') as file:
    with open('new_text_file.txt' , 'w') as new_file:
        for line in file:
            new_file.write(line)


new_file.close()
print(file.closed)