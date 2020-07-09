from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [Item("explorer skeleton", "looks like others have tried before...")],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [
            Item("unlit torch", "a torch without lighter fluid or flame"),
            Item("flint", "can be used to make a spark"),
        ],
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
        [
            Item("bucket of lighter fluid", "used to power the torch flame"),
            Item("samurai helmet", "adds +10 def when equipped"),
        ],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [
            Item("empty treasure chest", "what a bummer..."),
            Item(
                "mysterious cluster of stones",
                "perhaps if we re-arrange these stones a secret will be revealed",
            ),
        ],
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
        "Dave",
        room["outside"],
        [
            Item("flask", "used to hold liquid"),
            Item("castle cave map", "can be used to view your surroundings"),
        ],
    )

    def print__player_status():
        print(f"PLAYER STATUS:\n{player}")

    # ============================START MOVEMENTS==============================

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    # HANDLES PLAYER MOVEMENTS, VIEWING MAP/INVENTORY
    def handle_single_commands(command):
        error_message = "Sorry, you can't go that direction"

        if command == "n":
            # do north stuff
            if not hasattr(player.current_room, "n_to"):
                print(error_message)

            else:
                player.current_room = player.current_room.n_to
                print(f"{player.name} enters {player.current_room.name}")

        elif command == "e":
            # do east stuff
            if not hasattr(player.current_room, "e_to"):
                print(error_message)

            else:
                player.current_room = player.current_room.e_to
                print(f"{player.name} enters {player.current_room.name}")

        elif command == "s":
            # do south stuff
            if not hasattr(player.current_room, "s_to"):
                print(error_message)

            else:
                player.current_room = player.current_room.s_to
                print(f"{player.name} enters {player.current_room.name}")

        elif command == "w":
            # do west stuff
            if not hasattr(player.current_room, "w_to"):
                print(error_message)

            else:
                player.current_room = player.current_room.w_to
                print(f"{player.name} enters {player.current_room.name}")

        # MAP FUNCTIONALITY
        elif command == "m":
            # SET THE DIRECTION TO BLANK WALL IF THERE IS NO ROOM IN THAT DIRECTION
            blank_wall = "a blank wall"
            if not hasattr(player.current_room, "n_to"):
                player.current_room.n_to = blank_wall
            if not hasattr(player.current_room, "e_to"):
                player.current_room.e_to = blank_wall
            if not hasattr(player.current_room, "s_to"):
                player.current_room.s_to = blank_wall
            if not hasattr(player.current_room, "w_to"):
                player.current_room.w_to = blank_wall

            # PRINT THE ROOMS IN EVERY DIRECTION
            print(f"{player.name} checks the map...")
            print(f"To the north: {player.current_room.n_to}")
            print(f"To the east: {player.current_room.e_to}")
            print(f"To the south: {player.current_room.s_to}")
            print(f"To the west: {player.current_room.w_to}")

        elif command == "i":
            print("\nCURRENT INVENTORY:")
            for item in player.items:
                print(f"Item: {item.name}\nDescription: {item.description}\n")

        else:
            print("\nCommand not recognized, please enter a valid command\n")

            # ============================END MOVEMENTS==============================

    # HANDLES TAKING/DROPPING ITEMS
    def handle_double_commands(commands):
        action = commands[0]
        item = commands[1]

        print(action)
        print(item)

    # HANDLE USER INPUT
    def handle_input():
        user_input = input(
            "\nNext command:\npress 'm' to view map\npress 'i' to view current inventory\n"
        )
        if user_input == "quit":
            print("You have abandoned the castle cave!")
            quit()

        # FOR JUST SINGLE CHARACTER COMMANDS (DIRECTION, VIEW MAP/INVENTORY)
        if len(user_input.split()) == 1:
            handle_single_commands(user_input)

        elif len(user_input.split(" ")) == 2:
            handle_double_commands(user_input.split(" "))

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # GAME LOOP
    while playing == True:
        print__player_status()
        handle_input()
        print("\n-------------------------------------------------------\n")


castle_quest()
