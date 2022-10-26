# Sprites
ui_wall = [
    "######",
    "######",
    "######",
    "######"
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

ui_apple = [
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

# Function that selects the starting map
def choose_map():

    # @ -> our hero
    # G -> ghosts
    # P -> pills
    # C -> cherry
    # . -> empty spaces
    # | and - -> walls

    # small
    map_small = [
    "|---------|",
    "|PG.....GP|",
    "|..|...|..|",
    "|....@....|",
    "|..|...|..|",
    "|PG.....GP|",
    "|---------|"
]

# medium
    map_medium = [
    "|------------------|",
    "|PG......GG......GP|",
    "|G................G|",
    "|...|P.||..||.P|C..|",
    "|..||..||..||..||..|",
    "|........@.........|",
    "|..................|",
    "|..||..||..||..||..|",
    "|..C|P.||..||.P|...|",
    "|G................G|",
    "|PG......GG......GP|",
    "|------------------|"
]

# large
    map_large = [
    "|------------------------------------|",
    "|G.......G.......P||P.......G.......G|",
    "|.||P||.||||.||||.||.||||.||||.||P||.|",
    "|.||P||...........||...........||P||.|",
    "|.......||C|.|.||.GG.||.|.|C||.......|",
    "|.||.||.||.|.|.||.||.||.|.|.||.||.||.|",
    "|@||.||.||........||........||.||.||.|",
    "|.......||.|||.||.GG.||.|||.||.......|",
    "|.||P||........C..||..C........||P||.|",
    "|.||P||.||||.||||.||.||||.||||.||P||.|",
    "|G.......G.......P||P.......G.......G|",
    "|------------------------------------|"
]

# special
    map_special = [
    "|----------------------------------|",
    "|PG......G....G.....@.....G......GP|",
    "|G................................G|",
    "|..|||..|||..|||..|||||..|||..|||..|",
    "|..|G|..|G|..|P...|C|C|..|G|..|C|..|",
    "|..|||..|||..|C...|P|P|..|||..|P|..|",
    "|..|C...|P|..|P...|.|.|..|P|..|.|..|",
    "|..|....|P|..|||..|.|.|..|P|..|.|..|",
    "|G................................G|",
    "|PG......G....G.....G.....G......GP|",
    "|----------------------------------|"
]
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
        map = map_small
        size = 1
    elif map_nr == "medium":
        map = map_medium
        size = 2
    elif map_nr == "large":
        map = map_large
        size = 3
    elif map_nr == "special":
        map = map_special
        size = 3
        
    return map, size

# Function that prints the map
def ui_print(map,pacman_state):
    for row in map:
        for piece in range(4):
            for column in row:
                if column == 'G':
                    print(ui_ghost[piece], end='')
                if column == 'P':
                    print(ui_apple[piece], end='')
                if column == 'C':
                    print(ui_cherry[piece], end='')
                if column == '@':
                    if pacman_state==0:
                        print(ui_pacman[piece], end='') # normal pacman
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

#Function that gets the key-input from the player
def ui_key():
    key = str(input())

    # check wrong input
    while key != "w" and key != "a" and key != "s" and key != "d":
        key = str(input())

    return key

# Loss Message
def ui_msg_lost(final_coins, final_ghosts, final_cherry):
    print("---")
    print("Pacman died, You lost!")
    final_score = final_coins + final_ghosts + final_cherry
    print ("Final Score: " + str(final_score) + " Points")
    print("---")

# Win Message
def ui_msg_win(final_coins, final_ghosts, final_moves, final_cherry):
    print("---")
    print("Congratulations, You won!")
    final_score = final_coins + final_ghosts + final_moves + final_cherry
    print ("Final Score: " + str(final_score) + " Points")
    print("---")

# Asks player if he would like to play again
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

