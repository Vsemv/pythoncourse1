# x = 5
# while x >= 1:
#     print(x)
#     x = x - 1

# x = 0
# while x < 10:
#     print(str(x) + ' x is less than 10')
#     x += 1
# else:
#     print(str(x) + ' x now is not less than 10')
    
# for x in range(10):
#     print(str(x) + ' x is less than 10')
# else:
#     x += 1
#     print(str(x) + ' x now is not less than 10')
    
# keywords: break, continue, pass

my_list = [1, 2, 3]

# for item in my_list:
#     if item == 2:
#         break
#     print('Another code')
# print('Some another code')

for item in my_list:
    if item == 2:
        continue
    print(item)
print('Another code')