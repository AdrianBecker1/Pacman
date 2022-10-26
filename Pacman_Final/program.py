from pacman import play, move_ghosts, total_pills, count_ghosts, total_cherry
from ui import ui_print, ui_key, ui_msg_win, ui_msg_lost, choose_map, play_again


def play_pacman ():

    player = True

    # while player wants to play
    while player:

        # get map
        map, size = choose_map()

        # get starting values
        start_coins = total_pills(map)
        start_moves = 0
        start_ghosts = count_ghosts(map)
        start_cherry = total_cherry(map)
        game_finished = False
        pacman_state = 0 # normal pacman sprite

        # while pacman did not die or did not eat all pills
        while not game_finished: 

            # print map
            ui_print(map,pacman_state)

            # get key
            key = ui_key()
            start_moves = start_moves + 1 # count moves of pacman

            #################################################################################################################################################################################
            # move pacman
            valid_key, pacman_alive, won = play(map, key)  # the three booleans from play_function
            
            # move ghosts
            pacman_was_hit = move_ghosts(map)
            #################################################################################################################################################################################

            # check if pacman died (was hit by ghost or hit a wall) & Ends the game
            if (not pacman_alive) or (pacman_was_hit):

                pacman_state = 1 # dead

                # print end map
                ui_print(map,pacman_state) 

                # calculate score
                end_coins = total_pills(map)
                end_ghosts = count_ghosts(map)
                end_cherry = total_cherry(map)
                final_coins = 50 * abs(end_coins - start_coins)
                final_ghosts = 100 * abs(end_ghosts - start_ghosts)
                final_cherry = 100 * abs(end_cherry - start_cherry)

                ui_msg_lost (final_coins, final_ghosts, final_cherry)

                game_finished = True

            # check if pacman won (was hit by ghost or hit a wall) & Ends the game
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

#############################
play_pacman() # Play Function
#############################