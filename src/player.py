# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"Name: {self.name}\nCurrent Room Name: {self.current_room.name}\n"

    # def try_direction(self, command):
    #     attribute = command + "_to"

    #     if hasattr(self.current_room, attribute):
    #         self.current_room = getattr(self.current_room, attribute)
    #     else:
    #         print("Cannot go that direction")
