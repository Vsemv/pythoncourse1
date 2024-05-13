class Swimmable:
    
    def __init__(self, name):
        print('Method init() of GameCharacter')
        self.name = name
        
    def greeting(self):
        print(f'Hello! My name is {self.name} and I can swim')
        
    def swim(self):
        print('I\'m swiming')
        
        
class Walkable:
    
    def __init__(self, name):
        print('Method init() of GameCharacter')
        self.name = name
        
    def greeting(self):
        print(f'Hello! My name is {self.name} and I can walk')
        
    def walk(self):
        print('I\'m walking')
        
        
class Flyable:
    
    def __init__(self, name):
        print('Method init() of GameCharacter')
        self.name = name
        
    def greeting(self):
        print(f'Hello! My name is {self.name} and I can fly')
        
    def fly(self):
        print('I\'m flying')
        
        
class GameCharacter(Walkable, Flyable, Swimmable):
    
    def __init__(self, name):
        print('Method init() of GameCharacter')
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)
        
    # def greeting(self):
    #     print(f'Hello! My name is {self.name}')
        
    
james = GameCharacter('James')
james.greeting()
# james.swim()
# james.walk()
# james.fly()

# print(isinstance(james, Walkable))
# print(isinstance(james, Swimmable))
# print(isinstance(james, Flyable))
# print(isinstance(james, GameCharacter))
# print(isinstance(james, dict))
# print(isinstance(james, object))
# print(isinstance(5, object))
# print(isinstance('dshesh', object))
# print(isinstance(('re', 5), object))
# print(isinstance({5, 'tyf', True}, object))

