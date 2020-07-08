from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#
def castle_quest():

    # WELCOME MESSAGE
    welcome_message = "==============================\nWelcome to the CASTLE CAVE!\n==============================\n"
    print(welcome_message)

    # ESTABLISH PLAYING STATUS
    playing = True

    # Make a new player object that is currently in the 'outside' room.
    player = Player(
        "Dave", room["outside"].name, ["flask", "castle map", "healing elixir"]
    )

    def print__player_status():
        print(f"PLAYER STATUS:\n{player}")

    # HANDLES PLAYER MOVEMENTS
    def handle_movements(command):
        if len(command.split()) == 1:
            print("hey")
        else:
            print("\nCommand not recognized, please enter a valid command\n")

    # HANDLE USER INPUT
    def handle_input():
        user_input = input("\nNext command:\npress 'h' for command help\n")

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # GAME LOOP
    while playing:
        print__player_status()
        handle_input()
        print("\n-------------------------------------------------------\n")


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


castle_quest()
