# immutable
first_name = "Jake"
print(first_name[2])
# first_name[2] = 'n' строки не изменяются
first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

# concatenable
new_first_name = first_two_letters + 'n' +last_letter
print(new_first_name)

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)
# multiplication
yummy = 'Yum '
print(yummy * 3)
# строки являются объектами
print(yummy.upper())
print(yummy.lower())

long_string = 'This is the long string'
print(long_string.split()) # разбить строку по словам. Запишется как объект
print(long_string.split('s'))