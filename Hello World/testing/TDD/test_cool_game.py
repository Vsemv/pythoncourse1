# TDD - Test Driven Development



import unittest
import cool_game



class CoolGmaeFunctionsTest(unittest.TestCase):
    def test_greet(self):
        """greet() have to return 'How are you?' if isEnemy == False"""
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')
    
    def test_greet_enemy(self):
        """greet() have to return 'I will kill bastard! if isEnemy == True"""
        self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill bastard!')
        
    def test_eat_burgers(self):
        """eat_burgers() have to return 'Mmm! Thas was excellent!' if number <= 3"""
        self.assertEqual(cool_game.eat_burgers(3), 'Mmm! Thas was excellent!')
        
    def test_eat_to_much_burgers(self):
        """eat_burgers() have to return 'Oh! I overate!' if number > 3"""
        self.assertEqual(cool_game.eat_burgers(4), 'Oh! I overate!')


if __name__ == '__main__':
    unittest.main()