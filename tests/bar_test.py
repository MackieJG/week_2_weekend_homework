import unittest

from classes.bar import *
from classes.guest import *
from classes.song import *
from classes.room import *

class TestBar(unittest.TestCase):
    def setUp(self):
        
        self.drink_1 = Bar("Beer", 5)
        self.drink_2 = Bar("Wine", 10)
        self.drink_3 = Bar("Gin", 7)

    def test_add_money_to_bar_tab(self):
        self.bar_tab = 0
        expected_output = 5
        actual_output = self.add_money_to_bar_tab(self.drink_1.price)
        self.assertEqual(expected_output, actual_output)