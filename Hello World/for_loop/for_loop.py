number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
#     print(str(number) + ' Hola!')
#     # print('Hola!')

# for num in number_list:
#     if num % 2 == 0:
#         print(num)
#     else:
#         print('num odd')

# list_number_sum = 0
# for number in number_list:
#     list_number_sum += number
# print(list_number_sum)

# for letter in 'Hello python!':
#     if letter != 'o':
#         print(letter)

# letter_sum = 0
# for letter in 'Hello python!':
#     print('One more letter =(')
#     letter_sum += 1
# print(letter_sum)

# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
#     print(item)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1, letter_2)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1)
#     print(letter_2)
# for letter_1, letter_2 in tuple_list:
#     print(letter_1)

# tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
# for letter_1, letter_2, number in tuple_list_1:
#     print(letter_1, letter_2, number)

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# # keys:
# for item in dictionary:
#     print(item)
# # keys-value pairs in tuples:
# for item in dictionary.items():
#     print(item)

# for item in dictionary.keys():
#     print(item)
# # values:
# for item in dictionary.values():
#     print(item)
# for key, value in dictionary.items():
#     print(value)

# for _ in range(5):
#     print('Hello!')

#           exercise:
int_sum = 0
for i in range(31):
    if i >= 10 and i % 2 == 0:
        int_sum = int_sum + i
print(int_sum)

user_num = int(input('write some number '))
for _ in range(user_num):
    print('Hello!')