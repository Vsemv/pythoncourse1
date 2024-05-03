# built-in functions
# x = print('Hello!')
# y = set()

# print(type(x))
# print(type(y))

# print(x)
# print(y)

# # built-in methods
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     '''
#     Print `Hello` text
#     :return: None
#     '''
#     print('Hello!')
# #   call the function
# print_greeting()
# #   receive the description of the function
# # help(print_greeting)

# def print_greeting_with_name(name = 'name'):
#     '''
#     :param name
#     :return: None
#     '''
#     print('Hello ' + name + '!')
# x = print(print_greeting_with_name('Jane'))
# print(x)

# def sum_of_two_numbers(a = 0, b = 0):
#     '''
#     :param a: The first addend
#     :param b: The second addend
#     :return: Sum of a and b
#     '''
#     return a + b
# x = sum_of_two_numbers(1, 1)
# print(x)

# def is_hello_in_text(text):
#     if 'hello' in text:
#         return True
#     else:
#         return False
# print(is_hello_in_text('say hello everyone'))

# def is_hello_in_text(text):
#     return 'hello' in text
# print(is_hello_in_text('say hello everyone'))

# def is_string_in_text(string, text):
#     return string in text
# print(is_string_in_text('hi', 'The apple'))

# def greeting_depends_of_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! you look great!')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nice!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'ve never seen the creature like you!')
#         return gender
    
    
# returned_value = greeting_depends_of_gender('Jacke', 'male')
# returned_value = greeting_depends_of_gender('Jane', 'female')
# returned_value = greeting_depends_of_gender('Mike', 'reptile')

# def greeting_depends_of_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! you look great!')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! You are so nice!')
#         return gender
#     else:
#         print('Hello ' + name + '! I\'ve never seen the creature like you!')
#         return gender
    
    
# returned_value_1 = greeting_depends_of_gender('Jacke', 'male')
# returned_value_2 = greeting_depends_of_gender('Jane', 'female')
# returned_value_3 = greeting_depends_of_gender('Mike', 'reptile')

# print(returned_value_1)
# print(returned_value_2)
# print(returned_value_3)

#           excercise

def cat_voice():
    print('Meow!')
    
def dog_voice():
    print('Woof!')
    
print(cat_voice())
print(dog_voice())

def cat_voice():
    x = 0
    while x < 2:
        print('Meow!')
        x += 1
    return 'Meow!'
print(cat_voice())

def dog_voice():
    x = 0
    while x < 2:
        print('Woof!')
        x += 1
    return 'Woof!'
print(dog_voice())

def get_voice(string):
    return string + '!'
print(get_voice('Hello'))

def generator_odd_numbers(number_a, number_b):
    return [number for number in range(number_a, number_b + 1) if number % 2 != 0 ]
odds = generator_odd_numbers(5, 31)
print(odds)

def generator_odd_numbers_1(number_c, number_d):
    odd = []
    for i in range(number_c, number_d + 1):
        if i % 2 == 1:
            odd.append(i)
    return odd
odds_2 = generator_odd_numbers_1(51, 101)
print(odds_2)