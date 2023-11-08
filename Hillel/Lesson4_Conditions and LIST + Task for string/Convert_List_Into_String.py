#Ви маєте список ['Hillel', 'AQA', 'TEST'], переведіть цей список в стрінгу, а потім знову в список

lst = ["Hillel", "AQA", "TEST"]
print(f"\nINITIAL LIST: {lst} \n")

conv_into_str = ", ".join(lst)
type_of_str = type(conv_into_str)
print(f"CONVERTED LIST INTO STR: {conv_into_str}, PROOF: {type_of_str} \n")

conv_into_list = conv_into_str.split(",")
type_of_lst = type(conv_into_list)
print(f"CONVERTED STR BACK TO LIST: {conv_into_list}, PROOF: {type_of_lst}")