rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(type(rainbow_colors))
print(rainbow_colors)
empty_set = set() # создать пустое множество
print(empty_set)
print(type(empty_set))

number_list =  [1, 43, 56, 3, 3, 3, 3]
text_tuple = ('fge', 'erge', 'rtyuq', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
set_from_list.add(777) # if the element already in use in "sets", this element is not added to the sets
set_from_tuple.add('hello') # if the element already in use in "sets", this element is not added to the sets

x = set_from_list.pop()
set_from_list.remove(3)
set_from_list.discard(43)
# set_from_list.remove(3)
set_from_list.discard(3)
set_from_list.clear()

print(set_from_list)
print(set_from_tuple)
print(x)


                # exercise:

set_text = set('blue')
print(set_text)
print(type(set_text))