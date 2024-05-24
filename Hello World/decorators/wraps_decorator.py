from functools import wraps



def print_function_data(function):
    """this is decorator function

    Args:
        function (_type_): _description_
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'You are useing {function.__name__}')
        print(f'Function documentation {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper
    
    
@print_function_data
def squares_sum(a, b):
    """squares sum

    Args:
        a (_int_): _first number_
        b (_int_): _second number_

    Returns:
        _int_: _sum of squares first and second number: (a*a+b*b)_
    """
    return a * a + b * b

    
print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
# help(squares_sum)