
ui_wall = [
    "......",
    "......",
    "......",
    "......"
]

ui_ghost = [
    " .-.  ",
    "| OO| ",
    "|   | ",
    "'^^^' "
]

ui_pacman = [
    " .--. ",
    "/ _.-'",
    "\\  '-.",
    " '--' "
]

ui_pacman_cherry = [
    " .--. ",
    "///.-'",
    "\\\\\\\'-.",
    " '--' "
]

ui_empty = [
    "      ",
    "      ",
    "      ",
    "      "
]

ui_pill = [
    "      ",
    " .--. ",
    " '--' ",
    "      "
]

ui_cherry = [
    "  __  ",
    " /  \\ ",
    ".I..I.",
    "'-''-'"
]

ui_dead = [
    " .--. ",
    "/.**.\\",
    "|RIP.|",
    "|____|"
]

ui_won = [
    ":----:",
    "':  :'",
    " 'II' ",
    " _II_ "
]


def choose_map(map1,map2,map3,map4):

    print("Welcome to Pacman! Please choose your Map-Size:")
    print(" *small* | *medium* | *large* | *special* ")
    map_nr = str(input())

    # check wrong input
    while map_nr != "small" and map_nr != "medium" and map_nr != "large" and map_nr != "special":
        print("---")
        print("Please try again!")
        print("---")
        map_nr = str(input())

    if map_nr == "small":
        map = map1
        size = 1
    elif map_nr == "medium":
        map = map2
        size = 2
    elif map_nr == "large":
        map = map3
        size = 3
    elif map_nr == "special":
        map = map4
        size = 3
        
    return map, size

def ui_print(map,pacman_state):
    for row in map:
        for piece in range(4):
            for column in row:
                if column == 'G':
                    print(ui_ghost[piece], end='')
                if column == 'P':
                    print(ui_pill[piece], end='')
                if column == 'C':
                    print(ui_cherry[piece], end='')
                if column == '@':
                    if pacman_state==0:
                        print(ui_pacman[piece], end='')
                    elif pacman_state==1:
                        print(ui_dead[piece], end='') # pacman is dead
                    elif pacman_state==2:
                        print(ui_won[piece], end='') # pacman won
                    elif pacman_state==3:
                        print(ui_pacman_cherry[piece], end='') # pacman with cherry
                if column == '.':
                    print(ui_empty[piece], end='')
                if column == '-' or column == '|':
                    print(ui_wall[piece], end='')

            print("")


def ui_key():
    key = str(input())

    # check wrong input
    while key != "w" and key != "a" and key != "s" and key != "d":
        key = str(input())

    return key

def ui_msg_lost(final_coins, final_ghosts, final_cherry):
    print("---")
    print("Pacman died, You lost!")
    final_score = final_coins + final_ghosts + final_cherry
    print ("Final Score: " + str(final_score) + " Points")
    print("---")


def ui_msg_win(final_coins, final_ghosts, final_moves, final_cherry):
    print("---")
    print("Congratulations, You won!")
    final_score = final_coins + final_ghosts + final_moves + final_cherry
    print ("Final Score: " + str(final_score) + " Points")
    print("---")


def play_again():
    print("Do you want to play again? (Y or N)")
    answer = str(input())
    
    # check for wrong input
    while answer != "Y" and answer != "N":
        print("---")
        print("Please try again:")
        answer = str(input())

    if answer =="Y":
        return True
    else:
        return False

