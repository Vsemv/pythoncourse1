# special (magic) methods __method_name__

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
        
    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname
    
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        return self.age + other.age
    
    def __del__(self):
        print('person object with name ' + self.firstname + ' is deleted from memory')
        
        
jack = Person('Jack', 'White', 45)

jane = Person('Jane', 'Eyre', 23)

print(jack + jane)

print([1, 2, 3, 4, 5])
print(jack)
print(len(jack))
# del (jack)

# x = 5
# y = 3
# a = '5'
# b = '3'
# print(x + y)
# print(x.__add__(y))
# print(a + b)
# print(a.__add__(b))



#           exercise


class Chain:
    
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items
        
    def __str__(self):
        return f'Chain with {self.number_of_items} items'
        
    def __len__(self):
        return self.number_of_items
    

box = Chain(3)
print(box)
print(len(box))