# print('Some code')
# print(my_variable)
# print(len(23))
# try:
#     print(len(23))
#     print(my_variable)
# except NameError:
#     print('NameError has happen')
# except TypeError:
#     print('TypeError has happen')
# print('Code after error')


user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}
# print(user_dictionary['first_name'])
# print(user_dictionary['name'])
# print(user_dictionary.get('last_name'))
# print(user_dictionary.get('name'))

def get_dictionary_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dictionary_value(user_dictionary, 'age'))
print(get_dictionary_value(user_dictionary, 'name'))
print(get_dictionary_value(user_dictionary, 'first_name'))