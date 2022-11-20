class Room:
    def __init__(self, name, entry_fee, room_capacity):
        self.name = name
        self.entry_fee = entry_fee
        self.room_capacity = room_capacity
        self.list_of_guests = []
        self.list_of_songs = []
        

    def guest_check_in(self, guest):
        if len(self.list_of_guests) < self.room_capacity:
            self.list_of_guests.append(guest)
        else: 
            return "No room at the inn sun"

    def remove_guest_from_room(self, guest):
        self.list_of_guests.remove(guest)
        
    def add_song_to_room(self, song):
        self.list_of_songs.append(song)

    def remove_song_from_room(self, song):
        self.list_of_songs.remove(song)

    def does_customer_have_enough_money(self, room_price, guest):
        if guest.wallet >= room_price:
            return True
        return False

    def song_on_room_playlist(self, guest):
        for item in self.list_of_songs:
            if guest.favourite_song == item.name:
                return "Whoo!"
            else:
                return "Unlucky"
