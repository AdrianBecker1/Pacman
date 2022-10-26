import random
from ui import ui_print, ui_key


# this function returns three booleans
# the first indicates whether the pressed key was a valid key
# the second indicates whether the pacman is still alive
# the third indicates whether the pacman won the game
def play(map, key):
    next_x, next_y = next_position(map, key)  #get the new position

    # check if input is a invalid key
    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key:
        return False, True, False # No movement , Game continues, not yet won

    # check if pacman is not within borders
    if not within_borders(map, next_x, next_y):
        return False, True, False # No movement , Game continues, not yet won

    # check if pacman is inside a wall
    if is_a_wall(map, next_x, next_y):
        return False, True, False # No movement , Game continues, not yet won

    # check if pacman touches a ghost
    is_a_ghost = map[next_x][next_y] == 'G'
    if is_a_ghost:
        return True, False, False # Movement , Game Finishes, not yet won

    # Get the remaining cherrys before pacman moves
    start_cherry = total_cherry(map)

    # move pacman
    move_pacman(map, next_x, next_y)

    # Get the remaining cherrys after pacman moves
    remaining_cherry = total_cherry(map)

    # check if pacman ate a cherry
    if start_cherry > remaining_cherry:
        finished = play_cherry(map)  # special cherry phase

        # ...and finish game if he ate all pills while in cherry-phase
        if finished == True:
            return  True, True, True   # Movement, Game continues, Win

    # check if pacman ate all pills
    remaining_pills = total_pills(map)

    if remaining_pills == 0:
        return True, True, True   # Movement, Game continues, Win   
    else:
        return True, True, False   # Movement, Game continues, not yet won


# special cherry phase if pacman ate a cherry
def play_cherry(map):
    
    count = 7 # Number of moves with cherry

    while count > 0:
        ui_print(map,3)
        count = count - 1
        key = ui_key()

        #get the new position
        next_x, next_y = next_position(map, key)

        # check if input is a invalid key
        is_an_invalid_key = next_x == -1 and next_y == -1
        if is_an_invalid_key:
            continue

        # check if pacman is not within borders
        if not within_borders(map, next_x, next_y):
            continue

        # check if pacman is inside a wall
        if is_a_wall(map, next_x, next_y):
            continue
        
        # no need to check for ghosts since they get deleted in this phase

        # Return true if pacman ate all pills
        move_pacman(map, next_x, next_y)

        # check if pacman ate all pills
        remaining_pills = total_pills(map)

        # Return true if pacman ate all pills
        if remaining_pills == 0:
            return True 

#################################################################################################################################################################################

# Finds the location of Pacman on the map
def find_pacman(map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y

# Function that move spacman after he was found on the map
def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)

    move_entities (map, pacman_x, pacman_y, next_pacman_x, next_pacman_y, "@")

# Calaculates the next postion of pacman
def next_position(map, key):
    x, y = find_pacman(map)
    next_x = -1
    next_y = -1

    if key == 'a':
        next_x = x
        next_y = y - 1
    elif key == 'd':
        next_x = x
        next_y = y + 1
    elif key == 'w':
        next_x = x - 1
        next_y = y
    elif key == 's':
        next_x = x + 1
        next_y = y

    return next_x, next_y

# Function that randomly moves every ghost on the map
def move_ghosts(map):
    all_ghosts = find_ghosts(map)  # Find Ghosts
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_directions = [
            [ghost_x, ghost_y + 1], #right
            [ghost_x, ghost_y - 1], #left
            [ghost_x - 1, ghost_y], #up
            [ghost_x + 1, ghost_y]  #down
        ]

        movement_tries = 0

        while movement_tries < 10:

            # select a random possible movement
            # and get the x,y of the movement
            random_number = random.randint(0, 3)
            next_ghost_x = possible_directions[random_number][0] #Trennung x & y
            next_ghost_y = possible_directions[random_number][1] #Trennung x & y

            # checks before actually moving it!
            if not within_borders(map, next_ghost_x, next_ghost_y):
                movement_tries = movement_tries + 1
            elif is_a_wall(map, next_ghost_x, next_ghost_y):
                movement_tries = movement_tries + 1
            elif is_a_ghost(map, next_ghost_x, next_ghost_y):
                movement_tries = movement_tries + 1
            elif is_a_apple(map, next_ghost_x, next_ghost_y):
                movement_tries = movement_tries + 1
            elif is_a_cherry(map, next_ghost_x, next_ghost_y):
                movement_tries = movement_tries + 1
            elif is_pacman(map, next_ghost_x, next_ghost_y):
                return True  # ghost kills pacman -> pacman_was_hit = True
            else:
                movement_tries = movement_tries + 11 # legal movement

        if movement_tries >= 11: # Bug Behebung
            move_entities (map, ghost_x, ghost_y, next_ghost_x, next_ghost_y, "G")

    return False # non-fatal movement -> pacman_was_hit = False

# finds all ghosts on the map to move them after pacman moved
def find_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x,y])

    return all_ghosts

#################################################################################################################################################################################
def move_entities(map, x, y, next_x, next_y, symbol): # symbol = G or @

     # the place where the entity was is now empty
    everything_to_the_left = map[x][0:y]
    everything_to_the_right = map[x][y+1:]
    map[x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the entity
    everything_to_the_left = map[next_x][0:next_y]
    everything_to_the_right = map[next_x][next_y+1:]
    map[next_x] = everything_to_the_left + str(symbol) + everything_to_the_right
#################################################################################################################################################################################


# Functions that check certain things / objects on the map

def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == '|' or map[next_x][next_y] == '-'
    return is_a_wall

def is_a_ghost(map, next_x, next_y):
    is_a_ghost = map[next_x][next_y] == 'G'
    return is_a_ghost

def is_a_apple(map, next_x, next_y):
    is_a_apple = map[next_x][next_y] == 'P'
    return is_a_apple

def is_a_cherry(map, next_x, next_y):
    is_a_cherry = map[next_x][next_y] == 'C'
    return is_a_cherry

def is_pacman(map, next_x, next_y):
    is_pacman = map[next_x][next_y] == '@'
    return is_pacman

# Function that checks if Pacman is inside
def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns

    return x_is_valid and y_is_valid # Returns True od False

# Counts the remaining pills
def total_pills(map): 
    total = 0
    for x in range(len(map)): 
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total = total + 1
    return total

# Counts the remaining cherrys
def total_cherry(map):
    total = 0
    for x in range(len(map)): 
        for y in range(len(map[x])):
            if map[x][y] == 'C':
                total = total + 1
    return total

# Counts the remaining ghosts
def count_ghosts (map): 
    ghosts = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                ghosts = ghosts + 1

    return ghosts

