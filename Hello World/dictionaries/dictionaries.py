# car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
# print(car_prices)
# print(car_prices['toyota'])
# car_prices['mazda'] = 4000
# print(car_prices)
# car_prices['opel'] = 2000
# print(car_prices)

# # delete key:
# del car_prices['toyota']
# print(car_prices)

# # del car_prices # this comand delete all dictionary
# car_prices.clear() # clear all keys but not delete dictionary
# print(car_prices)


person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])

print(person['hobbies'][2])

children = person['children']
print(children)

print(person['children']['son'])

person['car'] = 'Mazda'
person['hobbies'][0] = 'basketball'
print(person.keys())
print(person.values())
print(person.items())

#   exercise

dictionary = {
    'name': 'Vitalik',
    'surame': 'Buterin'
}
print(dictionary['surame'])

pc_info = {
    'name': 'Dell',
    'screen resolution': '1920x1080',
    'F button functions': {'f1': 'sound off', 'f2': 'reduce sound', 'f3': 'increase sound'}
}
print(pc_info['F button functions']['f2'])