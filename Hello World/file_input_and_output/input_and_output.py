# # Input
# x = input('Input something ')
# # Output
# print('Output something ' + x)


# print(1, 2, 3, sep=':', end='\n')
# print(1, 2, 3, sep=',', end=' ')
# print(1, 2, 3, sep=';', end='')


# lorem_ipsum_text = open('/home/vsemeniuk/Desktop/LPython/sample.txt', 'r')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()


# lorem_ipsum_text = open('/home/vsemeniuk/Desktop/LPython/sample.txt', 'r')
# for line in lorem_ipsum_text:
#     if 'mary' in line.lower():
#         print(line, end='')
# lorem_ipsum_text.close()


# with open('/home/vsemeniuk/Desktop/LPython/sample.txt', 'r') as lorem_ipsum_text_1:
#     for line in lorem_ipsum_text_1:
#         if 'mary' in line.lower():
#             print(line, end='')


# with open('/home/vsemeniuk/Desktop/LPython/sample.txt', 'r') as lorem_ipsum_text_2:
#     line = lorem_ipsum_text_2.readline()
#     while line:
#         print(line, end='')
#         line = lorem_ipsum_text_2.readline()


# with open('/home/vsemeniuk/Desktop/LPython/sample.txt', 'r') as lorem_ipsum_text_3:
#     lines = lorem_ipsum_text_3.readlines()
# print(lines)

# for line in lines[::-1]:
#     print(line)


with open('/home/vsemeniuk/Desktop/LPython/sample.txt', 'r') as lorem_ipsum_text_3:
    text = lorem_ipsum_text_3.read()
print(text)