my_list = (input("Enter sentence, use space as separator: ")).split()
word_count = 0
start_index = 0
list_end_index = len(my_list) - 1

#Here is option how to make it with through cycle "for"
#for n in range(0, len(my_list)-2):
#    start_index = n
#    end_index = n + 3
#
#    for i in my_list[start_index:end_index]:
#        if i.isalpha():
#            word_count += 1
#
#    if word_count == 3:
#        break
#    else:
#        word_count = 0

while word_count != 3:
    word_count = 0
    for i in my_list[start_index:start_index + 3]:
        if i.isalpha():
            word_count += 1

    start_index += 1
    if start_index == list_end_index:
        break

if word_count == 3:
    print("True. The sentence has 3 words in a row.")
else:
    print("False. There aren't 3 words in the sentence.")
