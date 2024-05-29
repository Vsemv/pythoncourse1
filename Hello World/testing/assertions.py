# Testing is writting the test code that checks bugs in our code
# Assertions


# assert 2 + 2 == 4
# assert 2 + 2 == 5, '2 + 2 must equals 4'


# def devide(a, b):
#     assert b != 0, 'b must not equals zero'
#     return a / b

# print(devide(2, 0))


# def multiply_positive_numbers(a, b):
#     assert a > 0 and b > 0, 'a and b must be positive'
#     print(a * b)
    
    
# multiply_positive_numbers(3, -5)


def get_acces(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff')
    
    
password_1 = input('Please input the password ')
get_acces(password_1)