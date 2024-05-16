# colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# with open('/home/vsemeniuk/Desktop/LPython/rainbow_colors_1.txt', 'w') as rainbow_colors:
#     for color in colors_list:
#         print(color, file=rainbow_colors)
        
colors_list_1 = []
with open('/home/vsemeniuk/Desktop/LPython/rainbow_colors_1.txt') as rainbow_colors_1:
    for color_1 in rainbow_colors_1:
        colors_list_1.append(color_1.strip('\n'))
        
print(colors_list_1)


with open('/home/vsemeniuk/Desktop/LPython/rainbow_colors_1.txt', 'a') as rainbow_colors_1:
    print('dark green', file=rainbow_colors_1)
    print('dark blue', file=rainbow_colors_1)