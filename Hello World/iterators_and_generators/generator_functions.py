# Generators are Iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions



# def my_function(x):
#     return x


# print(my_function(5))


# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1
        
# print(count_up_to(4))
# counter = count_up_to(4)
# # print(counter.__next__())
# # print(counter.__next__())
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# counter = count_up_to(10)
# print(list(count_up_to(7)))

# for number in count_up_to(10):
#     print(number)
    
# counter.__next__()
# counter.__next__()

# for number in counter:
#     print(number)
    
    
    
#           excercise


def get_week_day():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    count = 0
    for day in days:
        yield day
        count += 1
        

current_day = get_week_day()
print(current_day.__next__()) # 'Sunday'
print(current_day.__next__()) # 'Monday'
print(current_day.__next__()) # 'Tuesday'
print(current_day.__next__()) # 'Wednesday'
print(current_day.__next__()) # 'Thursday'
print(current_day.__next__()) # 'Friday'
print(current_day.__next__()) # 'Saturday'


def even_odd():
    num = ['even', 'odd']
    count = 0
    for number in num:
        yield number
        count 