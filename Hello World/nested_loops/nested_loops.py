smile = '\U0001f600'
# for number in range(10):
#     count = 0
#     emotions = ''
#     while count <= number:
#         emotions += smile
#         count += 1
#     print(emotions)

# for number in range(10):
#     emotions = ''
#     for count in range(number + 1):
#         emotions += smile
#     print(emotions)

for number in range(1, 11):
    print(smile * number)
    
count = 1
while count < 11:
    print('\U0001f600' * count)
    count += 1