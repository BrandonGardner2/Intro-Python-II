import os

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
    run_game(f"Welcome {user_name}")


def run_game(message=""):
    os.system('cls')
    os.system('clear')
    print(player.__str__())
    if message:
        print(f"******{message}******")
    user = input(
        'Enter a cardinal direction. N, W, S, or E\nAlternatively, you can get/take or use followed by an item name\n')
    handle_input(user)


def handle_input(_input):
    if _input == "q" or _input == "Q":
        quit_game()
    else:
        valid_directions = ("n", "w", "e", "s")
        valid_item_uses = ("get", "take", "use")
        _input = _input.lower().split(' ')

        if _input[0] in valid_directions:
            handle_direction(f"{_input[0]}_to")
        elif _input[0] in valid_item_uses:
            handle_item(_input[0], _input[1])
        else:
            error_handler("Invalid input.")


def handle_direction(direction):
    try:
        player.location = player.location.__getattribute__(direction)
        run_game()
    except AttributeError:
        run_game("There are no rooms in that direction.")


def handle_item(action, item):
    if action == "get" or "take":
        if item in player.location.items:
            player.location.items.remove(item)
            player.inventory.append(item)
        else:
            error_handler("There is no item with that name, in this room.")
    else:
        if item in player.inventory:
            print("Item exists, do stuff")
        else:
            print("You don't have any items with that name")
    run_game()


def error_handler(error="There was an error!"):
    run_game(error)


def quit_game():
    print("Thanks for playing!")
    exit()


initialize_game()
