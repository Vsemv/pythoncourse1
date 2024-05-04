# *args - argument
# **kwargs - keyword arguments

# def ten_percent_of_product(x, y, z):
#     return (x * y* z) * 0.1
# print(ten_percent_of_product(10, 20, 7, 2))

# #                   *args
# def func_with_args(*args):
#     print(args)
# func_with_args(1, 2, 3)


# #                   **kwargs
# def func_with_kwargs(**kwargs):
#     print(kwargs)





# func_with_kwargs(first=1, second=2, third=3)

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1

# print(ten_percent_of_product_with_args(10, 20, 7))



# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent

# print(percent_of_product_with_args(20, 10, 20, 7))


# def func_with_kwargs(**kwargs):
#     print(kwargs)

# func_with_kwargs(first=1, second=2, third=3)

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')


# hello_with_kwargs(Gender='male', age=24, name='Jack')
# hello_with_kwargs(Gender='male', age=24)


# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
#     else:
#         print('{}! What is your name?'.format(greeting))


# hello_with_greeting_and_kwargs('Hello', Gender='male', age=24, name='Jack')
# hello_with_greeting_and_kwargs('Hey', Gender='male', age=24)


# def func_with_args_and_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['food']))
# func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')


#                   excercise:

def is_cat_here(*args):
    string = 'cat'
    for word in args:
        if string.lower() in word.lower():
            return True
    return False
        
print(is_cat_here('dog', 'monkey', 'cAt', 'carrot', 'purple'))


def is_item_here(item, *args):
    for word in args:
        if word == item:
            return True
    return False

print(is_item_here('Hello, its me', 'Hi Miley', 'Hello its you', 'Hello, its me', 24, 'Good', 'local'))


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))

your_favorite_color('blue', car='mazda', color='yellow', car_miliage=473000)