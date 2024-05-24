from time import time
from functools import wraps



# start_time = time.time()
# sum([number for number in range(1000000)])
# end_time = time.time() - start_time

# start_time_1 = time.time()
# sum(number for number in range(1000000))
# end_time_1 = time.time()


def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f'Time of code execution {end_time - start_time}')
        return result
    return wrapper


@speed_test
def sum_with_list():
    return sum([number for number in range(10000000)])


@speed_test
def sum_with_gen():
    return sum(number for number in range(10000000))


@speed_test
def product(range_value):
    result = 1
    for number in range(1, range_value):
        result *= number
    return result

print(sum_with_list())
print(sum_with_gen())
# print(product(1000))



#           excercise


def hello_from_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('the decorated function: ' + str(func(*args)))
        return print('Hello from decorator!')
    return wrapper

@hello_from_decorator
def decorated_function(string):
    return string


decorated_function('decorated')