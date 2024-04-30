# tuple_1 = (1, 2, 3)
# tuple_2 = 'one', 'hello'
# tuple_3 = (3, 2.3, 'three')

# print(tuple_1)
# print(tuple_2[1])
# print(type(tuple_2))
# print(tuple_3)

# #       tuple не изменяются
# # tuple_2[0] = 'Ihor'
# # print(tuple_2)
# #       что б изменить тапл, например, можно:
# new_tuple = ('Ihor', tuple_2[1])
# print(new_tuple)

#       распаковка данных в tuple:
# x = y = z = 12
# x, y, z = 12, 13, 14
# print(x, y, z)
person_tuple = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))

greetings_tuple = ('hi', 'hello', 'hi', 'hey')
print(greetings_tuple.count('hi'))
print(t1.index(5))
print(greetings_tuple.index('hey'))

#           excercise

computer_tuple = 'dell', 'xps', 'grey', 14
brand, model, color, display = computer_tuple
print(type(computer_tuple))
print(brand, model, color, display)
