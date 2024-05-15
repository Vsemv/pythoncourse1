# import random

# x = random.randint(1, 10)
# print(x)

from random import randint

x = randint(1, 10)
print(x)

# from random import shuffle
# my_list = ['x', 'z', 'y', 'a', 'b']
# shuffle(my_list)
# print(my_list)


from random import shuffle as shuffle_my_list
my_list = ['x', 'z', 'y', 'a', 'b']
shuffle_my_list(my_list)
print(my_list)



#           exercise

import math

number = 123456789
square_root = math.sqrt(number)
print(number)

number_factorial = 987
factorial_result = math.factorial(number_factorial)
print(factorial_result)

num = 876
exp = 54
print(math.pow(num, exp))