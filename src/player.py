# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(self):
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name}\n {self.current_room}"

    def move(self, direction):
        next_room = getaddr(self.current_room, f"{direction}_to")
        if next_room != None:
            self.current_room = next_room
        else:
            print("Not allowed. Try a different direction.")
