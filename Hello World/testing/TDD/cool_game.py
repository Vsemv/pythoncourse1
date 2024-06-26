from random import choice


def greet(name, isEnemy):
    if not isinstance(isEnemy, bool):
        raise ValueError('isEnemy must be a boolean type')
    if isEnemy:
        return f'Hello {name}! I will kill bastard!'
    else:
        return f'Hello {name}! How are you?'


def eat_burgers(number):
    if number > 3:
        return 'Oh! I overate!'
    else:
        return 'Mmm! Thas was excellent!'
    
    
def can_fly(name):
    if name == 'Batman':
        return True
    else:
        return False
    
    
def get_arsenal():
    return choice(('knife', 'handgun', 'machine gun'))