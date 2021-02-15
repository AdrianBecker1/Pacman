from pacman import play, move_ghosts, count_coins, count_ghosts, total_cherry
from ui import ui_print, ui_key, ui_msg_win, ui_msg_lost, choose_map


# @ -> our hero
# G -> ghosts
# P -> pills
# C -> cherry
# . -> empty spaces
# | and - -> walls

map1 = [
    "|---------|",
    "|PG.....GP|",
    "|..|...|..|",
    "|....@....|",
    "|..|...|..|",
    "|PG.....GP|",
    "|---------|"
]
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


map, size = choose_map(map1,map2,map3,map4)

start_coins = count_coins(map)
start_moves = 0
start_ghosts = count_ghosts(map)
start_cherry = total_cherry(map)
game_finished = False

pacman_state = 0


while not game_finished: # while not false == while true
    ui_print(map,pacman_state)
    key = ui_key()
    start_moves = start_moves + 1
    valid_key, pacman_alive, won = play(map, key)  # the three booleans from play_function

    pacman_was_hit = move_ghosts(map)

    if (not pacman_alive) or (pacman_was_hit): # (pacman_alive = false) or (pacman_was_hit = True)
        pacman_state = 1
        ui_print(map,pacman_state)   # end map
        end_coins = count_coins(map)
        end_ghosts = count_ghosts(map)
        end_cherry = total_cherry(map)
        final_coins = 50 * abs(end_coins - start_coins)
        final_ghosts = 100 * abs(end_ghosts - start_ghosts)
        final_cherry = 100 * abs(end_cherry - start_cherry)
        ui_msg_lost (final_coins, final_ghosts, final_cherry)
        game_finished = True

    elif won:
        pacman_state = 2
        ui_print(map,pacman_state)   # end map
        end_coins = count_coins(map)
        end_ghosts = count_ghosts(map)
        end_cherry = total_cherry(map)
        final_coins = 50 * abs(end_coins - start_coins)
        final_ghosts = 100 * abs(end_ghosts - start_ghosts)
        final_moves = (50 * size - start_moves) * 10
        final_cherry = 100 * abs(end_cherry - start_cherry)
        ui_msg_win (final_coins , final_ghosts, final_moves, final_cherry)     
        game_finished = True
