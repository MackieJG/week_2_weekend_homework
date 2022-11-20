import unittest

from classes.guest import *
from classes.room import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Andrew", "forever blue", 50)
        self.guest_2 = Guest("Megan", "I walk the line", 50)
        self.guest_3 = Guest("Flora", "desert cruiser", 50)

        self.room_1 = Room("Red", 10, 2)
        self.room_2 = Room("Blue", 80, 3)
        self.room_3 = Room("Yellow", 30, 3)

        self.song_1 = Song("forever blue")
        self.song_2 = Song("I walk the line")
        self.song_3 = Song("desert cruiser")
        self.song_4 = Song("heaven above")
        self.song_5 = Song("bladder")

    
    def test_room_has_name(self):
        self.assertEqual("Red", self.room_1.name)
    
    def test_room_1_capacity(self):
        self.assertEqual(2, self.room_1.room_capacity)

    def test_guest_check_in(self):
        self.room_1.guest_check_in(self.guest_1)
        self.assertEqual(1, len(self.room_1.list_of_guests))

    def test_remove_guest_from_room(self):
        self.room_2.guest_check_in(self.guest_2)
        self.room_2.remove_guest_from_room(self.guest_2)
        self.assertEqual(0, len(self.room_2.list_of_guests))
    
    def test_add_song_to_room(self):
        self.room_3.add_song_to_room(self.song_3)
        self.assertEqual(1, len(self.room_3.list_of_songs))

    def test_remove_song_from_room(self):
        self.room_3.add_song_to_room(self.song_3)
        self.room_3.remove_song_from_room(self.song_3)
        self.assertEqual(0, len(self.room_3.list_of_songs))

    def test_room_is_at_capacity(self):
        self.room_2.guest_check_in(self.guest_1)
        self.room_2.guest_check_in(self.guest_2)
        self.room_2.guest_check_in(self.guest_3)
        self.assertEqual(3, self.room_2.room_capacity)
   
    def test_refusing_guest_based_capacity(self):
        self.room_2.guest_check_in(self.guest_1)
        self.room_2.guest_check_in(self.guest_2)
        self.room_2.guest_check_in(self.guest_3)
        self.room_2.guest_check_in(self.guest_3)
        self.assertEqual(3, len(self.room_2.list_of_guests))

    def test_does_customer_have_enough_money(self):
        actual_output = self.room_1.does_customer_have_enough_money(self.room_1.entry_fee, self.guest_1)
        self.assertEqual(True, actual_output)
        

    def test_does_not_have_enough_money(self):
        actual_output = self.room_2.does_customer_have_enough_money(self.room_2.entry_fee, self.guest_1)
        self.assertEqual(False, actual_output)

    def test_song_on_room_playlist(self):
        self.room_2.add_song_to_room(self.song_2)
        self.room_2.add_song_to_room(self.song_3)
        self.room_2.add_song_to_room(self.song_1)
        expected_output = "Whoo!"
        actual_output = self.room_2.song_on_room_playlist(self.guest_2)
        self.assertEqual(expected_output, actual_output)