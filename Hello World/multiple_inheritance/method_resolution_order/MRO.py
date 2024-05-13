# Method Resolution Order

#     A
#    / \
#   B   C
#    \  /
#     D


class A:
    def some_method(self):
        print('Method of class A')
        

class B(A):
    def some_method(self):
        print('Method of class B')
        
        
class C(A):
    def some_method(self):
        print('Method of class C')
        
        
class D(B, C):
    pass
    # def some_method(self):
    #     print('Method of class D')
        

# to find out from which class the method will be called: __mro__, mro(), help()   :
# print(D.__mro__)
# print(D.mro())
help(D)

some_object = D()
some_object.some_method()