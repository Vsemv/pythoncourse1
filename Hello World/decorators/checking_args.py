from functools import wraps



# def prohibit_kwargs(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError('Keyword arguments are prohibited')
#         return func(*args, **kwargs)
#     return wrapper


# def prohibit_int_arguments(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for val in args:
#             if type(val) == int:
#                 raise ValueError('Integer arguments are prohibited')
#         for key, val in kwargs.items():
#             if type(val) == int:
#                 raise ValueError('Integer arguments are prohibited')
#         return func(*args, **kwargs)
#     return wrapper


# @prohibit_int_arguments
# def print_hello(name):
#     print(f'Hello {name}!')
    

# print_hello('Jack')
# print_hello(3)



#           excercise


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) <= 2:
            return func(*args, **kwargs)
        else:
            raise ValueError('Function must have less than 3 arguments!')
    return wrapper


@prohibit_more_than_2_args
def say_hi(first_name, second_name, who):
    print(f'Hi {first_name} {second_name}!')
    
    
say_hi('Mark', 'Twen', 'Writer')