# class num:
#     def __init__(self, int):
#         self.int = int
#     def count(self, degree):
#         res = 1
#         if self.int == 0:
#             return 0
#         for i in range(abs(degree)):
#             res *= self.int
#         return 1 / res if degree < 0 else res
    
# number = num(6)
# print(number.count(-3))


class Gamer:
    
    active_gamers = 0
    
    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers
    
    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)
    
    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1
        
    def ger_nickname(self):
        return self.nickname
    
    def get_age(sef):
        return sef.age
    
    def get_level(self):
        return self.level
    
    def get_points(self):
        return self.points
    
    def is_adult(self):
        return self.age >= 18
    
    def get_adult_lever_permission(self):
        if self.is_adult():
            print('You can go to adult level!')
        else:
            print('You can\'t go to adult level!')
            
    def log_out(self):
        Gamer.active_gamers -= 1

# print(Gamer.active_gamers)
# gamer_1 = Gamer('Hellboy', 23, 5, 13)
# print(Gamer.active_gamers)
# gamer_2 = Gamer('HarryPotter', 13, 7, 34)
# print(Gamer.active_gamers)

# print(gamer_1.get_age())
# print(gamer_1.get_adult_lever_permission())

# print(gamer_2.get_age())
# print(gamer_2.get_adult_lever_permission()) 

# gamer_2.log_out()
# print(Gamer.active_gamers)

# print(Gamer.get_active_gamers())

# james = Gamer.gamer_from_string('James, 34, 2, 45')
# jane = Gamer.gamer_from_string('Jane, 24, 3, 5')
# print(james.get_age())
# print(jane.get_level())
# print(Gamer.get_active_gamers())

my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'banana'))
print(my_dict)