# number_list = [32, 21, 48, 34.56]
# print(number_list)
# some_list = [12, 35.334, 'hello']
# print(some_list)
# print(len(some_list))
# print(some_list[1])
# another_list = some_list[:2]
# print(another_list)
# some_list[2] = 'hi'
# print(some_list)
# new_list = some_list + another_list
# print(new_list)

# #   adding items

# # new_list[5] = 'new item'
# new_list.append('new item')
# new_list.insert(0, 'start')
# new_list.insert(2, 13)

# #   removing items

# # new_list.pop()
# # new_list.pop(0)
# # new_list.pop(-3)

# deleted_item = new_list.pop(-3)
# deleted_item = new_list.remove(12)

# print(new_list)
# print(deleted_item)


# number_list = [45, 12,  3, -455, 22]
# letter_list = ['s', 'w', 't', 'a']

# new_list = letter_list.sort() # метод .sort() не возвращает значения
# print(new_list)

# чтобы получить отсортированный список надо:
# letter_list.sort()
# new_list = letter_list
# print(new_list)

# number_list.sort()
# letter_list.sort()

# number_list.reverse()
# letter_list.reverse()

# number_list.append(letter_list)

# print(number_list)
# print(letter_list)

#       exercise:

some_list = [45, 'text', 'gold', 23, 'apple', -545, 'word']
cut_item = some_list[:3]
print(cut_item)