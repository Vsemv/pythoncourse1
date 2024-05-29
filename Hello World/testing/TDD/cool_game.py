def greet(name, isEnemy):
    if isEnemy:
        return f'Hello {name}! I will kill bastard!'
    else:
        return f'Hello {name}! How are you?'


def eat_burgers(number):
    if number > 3:
        return 'Oh! I overate!'
    else:
        return 'Mmm! Thas was excellent!'