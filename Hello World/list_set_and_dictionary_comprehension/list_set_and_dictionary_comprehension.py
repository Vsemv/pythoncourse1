# greeting = 'hello!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)

# letter_list = [letter for letter in greeting]
# print(letter_list)
# number_list = [number for number in '0123456789']
# print(number_list)
# number_list_1 = [num for num in range(0, 10)]
# print(number_list_1)
# number_list_2 = [num ** 2 for num in range(0, 10)]
# print(number_list_2)
# number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(0, 10)]
# print(number_list_3)

# number_list = [6, 43, -2, 11, -55, -12, 3, 345]
# new_list = [number for number in number_list if number > 0]
# print(new_list)
# new_list_1 = ['+' if number > 0 else '-' for number in number_list]
# print(new_list_1)

#           exercise

# greetings = ['hello', 'hi', 'hey', 'hola']
# list_of_2nd_words = []
# for word in greetings:
#     list_of_2nd_words += word[1]
# print(list_of_2nd_words)

# greeting = ['hello', 'hi', 'hey', 'hola']
# list_of_2nd_words_1 = [word[1] for word in greeting]
# print(list_of_2nd_words_1)

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_digits = []
# for i in digits:
#     if i % 2 != 0:
#         new_digits.append(i)
# print(new_digits)

# digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_digit = [number for number in digit if number % 2 != 0]
# print(new_digit)



#                                   dictionary comprehension

# number_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key: value ** 3 for key, value in number_dict.items()}
# print(new_dict)

# number_list = [6, 43, -2, 11, -55, 0, -12, 3, 345]
# number_dict_1 = {number: number ** 2 for number in number_list}
# print(number_dict_1)

# number_dict_2 = {number: 'positive' if number > 0 else 'negative' if number < 0 else 'zero' for number in number_list}
# print(number_dict_2)



#                                   set comprehension

number_set_list = [3, 4, 7, 9, 8, -2, 0]
set_number_list = {number ** 2 for number in number_set_list}
print(set_number_list)

letter_set = {letter.upper() for letter in 'hello'}
print(letter_set)