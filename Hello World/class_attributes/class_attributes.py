class Car:
    
    wheels_number = 4
    
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        
        
mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)

print(mazda_car.name)
print(mazda_car.is_crashed)
print(mazda_car.wheels_number)

bmw_car = Car(name='BMW', color='black', year=2018, is_crashed=False)
print(bmw_car.name)
print(bmw_car.year)
print(bmw_car.wheels_number)

number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)

#           exercise:

class BlogPost:
    user_name = 'HellBoy'
    def __init__(self, text, number_of_likes):
        self.text = text
        self.number_of_likes = number_of_likes
        

blog_about_nature = BlogPost(text='tree', number_of_likes=5)
blog_about_animals = BlogPost(text='horse', number_of_likes=4)
blog_about_animals.number_of_likes = 6
print(blog_about_nature.number_of_likes)
print(blog_about_animals.number_of_likes)