import os
from mechanics import Move, Result

def start_game(player, opponent, pot=1000, pool=100, max_round=10):
    player.reset()
    opponent.reset()
    rnd = 1
    update_interface(player, opponent, pot, pool, rnd)
    
    while pot > 0 and rnd < max_round:
        user_choice = get_user_input()
        deduct, game_log = play_round(player, opponent, user_choice, pool)
        pot -= deduct
        rnd += 1
        if rnd == max_round:
            update_interface(player, opponent, pot, pool, 'END')
        else:
            update_interface(player, opponent, pot, pool, rnd)
        print(game_log)


def get_user_input():
    while True:
        user_choice = input("# Enter action: ")
        if "split" in user_choice.lower():
            user_choice = Move.SPLIT
            break
        elif "steal" in user_choice.lower():
            user_choice = Move.STEAL
            break
        elif "quit" in user_choice.lower() or user_choice.lower() == "q":
            exit()
        else:
            print("# Invalid input. Please try again.")
            continue
    return user_choice


# Play the round
def play_round(player, opponent, player_choice, pool):
    # Observe the opponent
    player.observe(opponent)
    opponent.observe(player)
    # Opponent choice
    opponent_choice = opponent.action()
    game_log = ""
    game_log += "# Player chooses " + player_choice.name + "\n"
    game_log += "# Opponent chooses " + opponent_choice.name + "\n"
    
    # Get result
    if player_choice == opponent_choice:
        # Both share
        if player_choice == Move.SPLIT:
            gains = int(pool / 2)
            player.update(player_choice, Result.SPLIT_WON, gains)
            opponent.update(opponent_choice, Result.SPLIT_WON, gains)
            game_log += "# Player gains " + str(gains) + " money\n"
            game_log += "# Opponent gains " + str(gains) +  " money\n"
        # Both steal
        else:
            player.update(player_choice, Result.STOLE_LOST, 0)
            opponent.update(opponent_choice, Result.STOLE_LOST, 0)
            pool = 0
            game_log += "# Player gains 0 money\n"
            game_log += "# Opponent gains 0 money\n"
    else:
        # Player steal
        if player_choice == Move.STEAL:
            player.update(player_choice, Result.STOLE_WON, pool)
            opponent.update(opponent_choice, Result.SPLIT_LOST, 0)
            game_log += "# Player gains " + str(pool) + " money\n"
            game_log += "# Opponent gains 0 money\n"
        # Opponent steal
        else:
            player.update(player_choice, Result.SPLIT_LOST, 0)
            opponent.update(opponent_choice, Result.STOLE_WON, pool)
            game_log += "# Player gains 0 money\n"
            game_log += "# Opponent gains " + str(pool) + " money\n"
    
    return pool, game_log


# Update interface
def update_interface(player, opponent, pot, pool, rnd):
    print_header()
    get_round_summary(player, opponent, pot, pool, rnd)


# Print header
def print_header():
    # Clear terminal output
    os.system('clear')
    # Header
    print_hashline()
    print("\t\t\t\tS P L I T")
    print("\t\t\t\t   O R")
    print("\t\t\t\tS T E A L")
    print_hashline()
    print()
    print("#\tPossible actions: 'split' or 'steal'")
    print("#\tEnter 'quit' or 'q' to quit")
    print()
    print_hashline()
    print()


# Print out the summary of the round
def get_round_summary(player, opponent, pot, pool, rnd):
    print("#\tROUND\t", rnd)
    print("#\tPOT\t", pot)
    print("#\tPOOL\t", pool)
    print()
    print_hashline()
    print()
    print("#\tPLAYER")
    get_player_info(player)
    print()
    print_hashline()
    print()
    print("#\tOPPONENT")
    get_player_info(opponent)
    print()
    print_hashline()
    print()


# Print player's money and previous three actions
def get_player_info(player):
    print("#\tMONEY\t", player.money)
    print("#\tPREV\t", [p.name for p in player.previous_actions[-3:]])


def print_hashline():
    # 24 #s
    print("#################################################################################")