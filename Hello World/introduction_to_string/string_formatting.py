# print(1 + 1)
# print('1' + '1')
# age = 23
# # print('Jack is ' + age + 'years old.') # можно конкатенировать только строку со строкой
# print('Jack is ' + str(age) + ' years old.') # можно привести переменну с числом в строковый тип и таким образом сконкатенировать число со строкой
# name = 'Jack'
# age = 23
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age) # {} - это индекс элемента в функции .format()
# print(name_and_age)
# week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'.format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# print(week_days)
# week_days_with_war = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}.' \
# .format(mo = 'Monday', tu = 'Tuesday', we = 'Wednesday', th = 'Thursday', fr = 'Friday', sa = 'Saturday', su = 'Sunday') # так же в .format() можно указать переменные к которым можно обращаться в {}
# print(week_days_with_war)

# float

# float_result = 1000 / 7
# print(float_result)
# print('The result of division is {0:1.3f}'.format(float_result)) # {0:1.3f} - это для того, что б сократить количество цифр после точки(float`a). В этом примере сокращено до 3
# print('''
#  {0:10.2f} {1:10.2f} {2:10.2f}
#  {3:10.2f} {4:10.2f} {5:10.2f}
#  {6:10.2f} {7:10.2f} {8:10.2f}
# '''.format(1.45778, 345.232352, 34.2344, 123.567, 324.123, 5768, 4545.35346, 235235, 3217.234))

# name = 'Jack'
# age = 23
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
# print(name_and_age)
# name_and_age = f'My name is {name}. I\'m {age} years old.' # можно заменить метод .format(), на f'{variable}'
# print(name_and_age)

# print('My name is %s. I\'m %d years old' % (name, age)) # старый метод форматирования строки из пайтон 2

# задание форматирование строк:
table_of_numbers = '''
{0:15.4f}{1:15.4f}{2:15.4f}{3:15.4f}
{4:15.4f}{5:15.4f}{6:15.4f}{7:15.4f}
'''.format(2.32534, 4.435543, 3.235346, 3.6875665, 4.5477567, 3.5475672, 8.543456, 7.453457)
print(table_of_numbers)