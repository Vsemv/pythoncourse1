# if we have an error - except block fires and else block doesn't fire
# if we have'n an error - else block fires and except block doesn't fire



# while True:
#     try:
#         number = int(input('Enter some number '))
#         print(number / 2)
#     except:
#         print('You have to enter a number!')
#     else:
#         print('Else block')
#         break
#     finally:                        # Finally block fires anyway
#         print('Finally block')    
    
# print('Code after error handling')


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print('You can\'t divide by zero' )
        print(e)
    except TypeError as e:
        print('x and y must be numbers')
        print(e)
    else:
        print('x was divided by y')
    finally:
        print('finally block')

# print(divide(4, 2))
# print(divide(4, 0))
print(divide(4, 'w'))