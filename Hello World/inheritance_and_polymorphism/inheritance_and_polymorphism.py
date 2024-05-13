# inheritance

# class Car:
#     wheels_number = 4
    
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
    
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
        
#     def change_color(self, new_color):
#         self.color = new_color
#         print('Color is changed to ' + new_color)
    
# class Truck(Car):
    
#     wheels_number = 6
    
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
        
#     def drive(self, city):
#         print('Truck ' + self.name + ' is driving to ' + city)
        
#     def load_cargo(self, weight):
#         print('The cargo is loaded. Weight is ' + str(weight) + ' kg')
    
        
# man_truck = Truck('Man', 'White', 2015, False)

# man_truck.drive('New York')
# print(man_truck.wheels_number)
# print(man_truck.color)
# man_truck.change_color('red')
# print(man_truck.color)
# man_truck.load_cargo(2000)



# polymorphism


# class Animal:
    
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         raise NotImplementedError('Class successor must implement this method')


# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(self.name + ' is saying woof')

       
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(self.name + ' is saying meow')
        

# class Mouse(Animal):
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(self.name + ' is saying pee-pee-pee')
        
        
# class Fish(Animal):
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(self.name + ' is saying nothing')

        
# spike = Dog('Spike')
# tom = Cat('Tom')
# jerry = Mouse('Jerry')
# freddy = Fish('Freddy')

# pet_list = [spike, tom, jerry, freddy]

# for pet in pet_list:
#     pet.speak()
    
    
# def pet_voice(pet):
#     pet.speak()
    
# pet_voice(spike)
# pet_voice(tom)
# pet_voice(jerry)

# pet_voice(freddy)



#           exercise


class GameCharacter:
    
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        
    def speak(self):
        print('Hi, my name is ' + self.name)
        
        
class Villain(GameCharacter):
    
    def __init__(self, name, health, level):
        super().__init__(name, health, level)
        
    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')
    
    def kill(self, character_to_kill: GameCharacter):
        character_to_kill.health = 0
        print('Bang-bang, now you\'re dead, ', character_to_kill.name)
        
        
xena = Villain('Xena', 100, 77)
print(xena.name)
print(xena.health)
print(xena.level)

loh = GameCharacter('Gerakl', 10000, 80)
loh.speak()

xena.speak()
xena.kill(loh)
print(loh.health)