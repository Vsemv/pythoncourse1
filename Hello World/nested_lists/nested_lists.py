neste_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, ['text', 'correct'], 13]]
# print(neste_list)
# print(len(neste_list))
# print(len(neste_list[2]))
# print(neste_list[3][3][1])
# print(len(neste_list[-1]))

#           print nested list

# for inner_list in neste_list:
#     print(inner_list)
    
# for i in neste_list:
#     for number in i:
#         print(number)

[[print(number) for number in inner_list] for inner_list in neste_list]