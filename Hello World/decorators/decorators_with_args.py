from functools import wraps
import time


def check_if_first_args_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec

@check_if_first_args_is('red')
def print_rainbow_colors(*colors):
    print(colors)
    
    
@check_if_first_args_is(7)
def multiply_7(a, b):
    return a * b
    
    
print_rainbow_colors('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')

print(multiply_7(8, 3))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)
        

print_text_n_times('Hi', '3')


@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))
print(divide('4', '2'))



#           excercise


def wait(n):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(n)
            print(f'There was a pause {n} seconds before execution {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@wait(3)
def square(a):
    print(a * a)
    
square(2)