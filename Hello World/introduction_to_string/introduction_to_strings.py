# greeting = "Hello"
# first_name = "Jack"
# last_name = "White"
# exclamation_sign = "!"
# whole_sentence = greeting + " " + first_name + " " + last_name + exclamation_sign
# print(whole_sentence)
# # excaping: \
# some_string = 'I\'m a programmer'
# print(some_string)
# string_with_new_lines = "Hello! \n \rMy name is Vova"
# print(string_with_new_lines)
# numbers = "1\t234567"
# print(numbers)

# # triple quotes
# string_with_triple_quotes = """This is text with "triple quotes" """
# wrapping_string_with_triple_quotes = """This is text 
# with 
# "triple quotes" """
# print(string_with_triple_quotes)
# print(wrapping_string_with_triple_quotes)

#               indexing and slicing in strings

# indexing
greeting = "Hello Python!"
greeting_length = len(greeting) # lent() длинна строки
print(greeting_length)
print(greeting[1])
print(greeting[-1]) # получить элемент строки с конца

# slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2]) # вывод букв с шагом (каждая вторая в этом случае)
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1]) # вывести строку наоборот
