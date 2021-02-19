from pacman import play, move_ghosts, total_pills, count_ghosts, total_cherry
from ui import ui_print, ui_key, ui_msg_win, ui_msg_lost, choose_map, play_again


# @ -> our hero
# G -> ghosts
# P -> pills
# C -> cherry
# . -> empty spaces
# | and - -> walls

# small
map1 = [
    "|---------|",
    "|PG.....GP|",
    "|..|...|..|",
    "|....@....|",
    "|..|...|..|",
    "|PG.....GP|",
    "|---------|"
]

# medium
map2 = [
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
map3 = [
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
map4 = [
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

def play_pacman (map1,map2,map3,map4):

    player = True

    # while player wants to play
    while player:

        map, size = choose_map(map1,map2,map3,map4)

        # get starting values
        start_coins = total_pills(map)
        start_moves = 0
        start_ghosts = count_ghosts(map)
        start_cherry = total_cherry(map)
        game_finished = False
        pacman_state = 0 # normal pacman sprite


        while not game_finished: # while not false == while true
            ui_print(map,pacman_state)
            key = ui_key()
            start_moves = start_moves + 1 # count moves of pacman

            # move pacman
            valid_key, pacman_alive, won = play(map, key)  # the three booleans from play_function
            # move ghosts
            pacman_was_hit = move_ghosts(map)

            if (not pacman_alive) or (pacman_was_hit): # (pacman_alive = false) or (pacman_was_hit = True)
                pacman_state = 1 # dead
                ui_print(map,pacman_state)   # end map

                # calculate score
                end_coins = total_pills(map)
                end_ghosts = count_ghosts(map)
                end_cherry = total_cherry(map)
                final_coins = 50 * abs(end_coins - start_coins)
                final_ghosts = 100 * abs(end_ghosts - start_ghosts)
                final_cherry = 100 * abs(end_cherry - start_cherry)

                ui_msg_lost (final_coins, final_ghosts, final_cherry)

                game_finished = True

            elif won:
                pacman_state = 2 # won
                ui_print(map,pacman_state)   # end map

                # calculate score
                end_coins = total_pills(map)
                end_ghosts = count_ghosts(map)
                end_cherry = total_cherry(map)
                final_coins = 50 * abs(end_coins - start_coins)
                final_ghosts = 100 * abs(end_ghosts - start_ghosts)
                final_moves = (50 * size - start_moves) * 10 # only count if won
                final_cherry = 100 * abs(end_cherry - start_cherry)

                ui_msg_win (final_coins , final_ghosts, final_moves, final_cherry)  

                game_finished = True
        
        player = play_again()

play_pacman(map1,map2,map3,map4)