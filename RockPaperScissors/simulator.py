from mechanics import Move, Result, compare

def simulate_game(player1, player2, round=5, print_rounds=False):
    player1.reset()
    player2.reset()
    for rnd in range(1, round+1):
        print("Round", rnd)
        simulate_round(player1, player2, print_rounds)
        print()
    if print_rounds:
        print("Player 1 honesty grade:", player1.honesty)
        print("Player 1 result:", player1.results)
        print("Player 2 honesty grade:", player2.honesty)
        print("Player 2 result:", player2.results)


def simulate_round(player1, player2, print_rounds):
    # Observe the opponent
    player1.observe(player2)
    player2.observe(player1)

    # Claims
    claim1 = player1.claim()
    claim2 = player2.claim()
    if print_rounds:
        print("Player 1 claims\t", claim1.name)
        print("Player 2 claims\t", claim2.name)
    
    # Choices
    choice1 = player1.choose(claim1)
    choice2 = player2.choose(claim2)
    if print_rounds:
        print("Player 1 uses\t", choice1.name)
        print("Player 2 uses\t", choice2.name)
    
    # Get results
    result = compare(choice1, choice2)
    if print_rounds:
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    
    # Update
    player1.update(claim1, choice1, Result(result))
    player2.update(claim2, choice2, Result(result * -1))