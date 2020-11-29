from mechanics import Move, Result

def simulate_game(player1, player2, pot=1000, pool=100, max_round=10, print_rounds=False):
    player1.reset()
    player2.reset()
    rnd = 1
    if print_rounds:
        print("Initial pot:", pot)
        print("Pool each round:", pool)
        print("Max round:", max_round)
        print()

    while pot > 0 and rnd <= max_round:
        if print_rounds:
            print("Round", rnd)
        deduct = simulate_round(player1, player2, pool, print_rounds)
        pot -= deduct
        rnd += 1
    
    if print_rounds:
        print("Player 1 has", player1.money, "money")
        print("Player 2 has", player2.money, "money")
        print("Remaining money left in pot:", pot)


def simulate_round(player1, player2, pool, print_rounds):
    # Observe the opponent
    player1.observe(player2)
    player2.observe(player1)

    # Select choice
    action1 = player1.action()
    action2 = player2.action()
    if print_rounds:
        print("Player 1 chooses", action1)
        print("Player 2 chooses", action2)
    
    # Get result
    if action1 == action2:
        # Both share
        if action1 == Move.SPLIT:
            gains = int(pool / 2)
            player1.update(action1, Result.SPLIT_WON, gains)
            player2.update(action2, Result.SPLIT_WON, gains)
            if print_rounds:
                print("Player 1 gains", gains, "money")
                print("Player 2 gains", gains, "money\n")
        # Both steal
        else:
            player1.update(action1, Result.STOLE_LOST, 0)
            player2.update(action2, Result.STOLE_LOST, 0)
            if print_rounds:
                print("No one gets anything\n")
            pool = 0
    else:
        # Player 1 steal
        if action1 == Move.STEAL:
            player1.update(action1, Result.STOLE_WON, pool)
            player2.update(action2, Result.SPLIT_LOST, 0)
            if print_rounds:
                print("Player 1 gains", pool, "money\n")
        # Player 2 steal
        else:
            player1.update(action1, Result.SPLIT_LOST, 0)
            player2.update(action2, Result.STOLE_WON, pool)
            if print_rounds:
                print("Player 2 gains", pool, "money\n")
    
    return pool