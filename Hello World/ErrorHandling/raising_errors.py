# raise ValueError('My invalid value')
# raise ValueError('')


# def get_rainbow_color(color_number):
        
#     color_number_list = [1, 2, 3, 4, 5, 6, 7]
#     if type(color_number) is not int:
#         raise TypeError('Color number must be integer type')
#     if color_number not in color_number_list:
#         raise ValueError('Color number must be in range of integer from 1 to 7')
    
#     if color_number == 1:
#         return 'red'
#     elif color_number == 2:
#         return 'orange'
#     elif color_number == 3:
#         return 'yellow'
#     elif color_number == 4:
#         return 'green'
#     elif color_number == 5:
#         return 'blue'
#     elif color_number == 6:
#         return 'indigo'
#     elif color_number == 7:
#         return 'violet'
    # else: raise ValueError('Invalid number')
    
    
# color = get_rainbow_color('erger')
# print(color)


def colorize_text(color_number, text):
        
    color_number_list = [1, 2, 3, 4, 5, 6, 7]
    if type(color_number) is not int:
        raise TypeError('Parameter color number must be integer type')
    if color_number not in color_number_list:
        raise ValueError('Parameter color number must be in range of integer from 1 to 7')
    if type(text) is not str:
        raise TypeError('Parameter text must be string type')
    
    if color_number == 1:
        print('red', text)
    elif color_number == 2:
        print('orange', text)
    elif color_number == 3:
        print('yellow', text)
    elif color_number == 4:
        print('green', text)
    elif color_number == 5:
        print('blue', text)
    elif color_number == 6:
        print('indigo', text)
    elif color_number == 7:
        print('violet', text)
    
    
print(colorize_text(2, True))