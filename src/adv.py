from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


def initialize_game():
    user_name = input("Welcome, please enter your name...\n")
    global player
    player = Player(user_name, room['outside'])
    run_game()


def run_game(message=""):
    print(player.__str__())
    if message:
        print(message)
    user = input('Enter a cardinal direction. N, W, S, or E\n')
    handle_input(user)


def handle_input(_input):
    if _input == "q" or _input == "Q":
        quit_game()
    else:
        valid_directions = ("n", "w", "e", "s")
        valid_item_uses = ()
        _input = _input.lower()

        if _input in valid_directions:
            handle_direction(f"{_input}_to")
        elif _input in valid_item_uses:
            handle_item(_input)
        else:
            error_handler()


def handle_direction(direction):
    try:
        player.location = player.location.__getattribute__(direction)
        run_game()
    except AttributeError:
        run_game("There are no rooms in that direction.")


def handle_item(item):
    print('Handling item usage')


def error_handler():
    run_game("Invalid input.")


def quit_game():
    print("Thanks for playing!")
    exit()


initialize_game()
