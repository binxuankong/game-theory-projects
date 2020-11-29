import os
from mechanics import Move, Result, compare

def start_game(player, opponent, rounds=10):
    player.reset()
    opponent.reset()
    rnd = 1
    
    while True:
        update_interface(player, opponent, rnd, rounds)
        if rnd == rounds+1:
            break
        # Observe the opponent
        player.observe(opponent)
        opponent.observe(player)
        # Get claim
        user_claim = get_user_input()
        # Escape sequence: to clear the input line
        print("\033[A                             \033[A")
        opponent_claim = opponent.random_choice()
        print("# Player claims to use", user_claim.name)
        print("# Opponent claims to use", opponent_claim.name)
        print()
        # Get choice
        user_choice = get_user_input(claim=False)
        # Escape sequence: to clear the input line
        print("\033[A                             \033[A")
        opponent_choice = opponent.random_strategy(opponent_claim)
        print("# Player uses", user_choice.name)
        print("# Opponent uses", opponent_choice.name)
        print()
        # Compare result
        # Result
        result = compare(user_choice, opponent_choice)
        if result == 0:
            print("# Tie!")
        elif result == 1:
            print("# Player wins!")
        else:
            print("# Opponent wins!")
        # Update
        rnd += 1
        player.update(user_claim, user_choice, Result(result))
        opponent.update(opponent_claim, opponent_choice, Result(result * -1))
        # Continue
        input("# Enter any key to continue ")


# Get user input for claim/choice
def get_user_input(claim=True):
    while True:
        if claim:
            user_choice = input("# Enter claim: ")
        else:
            user_choice = input("# Enter choice: ")
        if "rock" in user_choice.lower() or user_choice.lower() == "r":
            user_choice = Move.ROCK
            break
        elif "paper" in user_choice.lower() or user_choice.lower() == "p":
            user_choice = Move.PAPER
            break
        elif "scissors" in user_choice.lower() or user_choice.lower() == "s":
            user_choice = Move.SCISSORS
            break
        elif "quit" in user_choice.lower() or user_choice.lower() == "q":
            exit()
        else:
            print("# Invalid input. Please try again.")
            continue
    return user_choice


# Update interface
def update_interface(player, opponent, rnd, rounds):
    print_header()
    get_round_summary(player, opponent, rnd, rounds)


# Print header
def print_header():
    # Clear terminal output
    os.system('clear')
    # Header
    print_hashline()
    print("\t\t\t\t    R O C K")
    print("\t\t\t\t   P A P E R")
    print("\t\t\t\tS C I S S O R S")
    print_hashline()
    print()
    print("#\tEach round, players claim what they will choose: rock/paper/scissors")
    print("#\tPlayers can then make their actual choice based on own/opponent's claim")
    print("#\tHonesty shows how much the player's claims match their choices: A/B/C/D/E")
    print("#\tPREV shows the previous 3 rounds claims/choices")
    print("#\tPossible actions: 'rock'/'r', 'paper'/'p' or 'scissors'/'s'")
    print("#\tEnter 'quit' or 'q' to quit")
    print()
    print_hashline()
    print()


# Print out the summary of the round
def get_round_summary(player, opponent, rnd, rounds):
    if rnd <= rounds:
        print("#\tROUND\t", rnd, "/", rounds)
    else:
        print("#\tROUND\t END")
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
    print("#\tRESULTS\t\t", ",  ".join("{}: {}".format(k, v) for k, v in player.results.items()))
    print("#\tHONESTY\t\t", player.honesty)
    print("#\tPREV CLAIMS\t", [p.name for p in player.previous_claims[-3:]])
    print("#\tPREV CHOICES\t", [p.name for p in player.previous_choices[-3:]])


def print_hashline():
    # 24 #s
    print("#######################################################################################")