# # Input
# x = input('Input something ')
# # Output
# print('Output something ' + x)


# print(1, 2, 3, sep=':', end='\n')
# print(1, 2, 3, sep=',', end=' ')
# print(1, 2, 3, sep=';', end='')


lorem_ipsum_text = open('/home/vsemeniuk/Desktop/LPython/sample.txt')
for line in lorem_ipsum_text:
    print(line)
lorem_ipsum_text.close()