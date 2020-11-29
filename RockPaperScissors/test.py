import random
from player import Player
from mechanics import *

num_games = 5

player1 = Player()
player2 = Player()

for i in range(num_games):
    # Observe
    player1.observe(player2)
    player2.observe(player1)
    # Claims
    claim1 = player1.random_choice()
    claim2 = player1.random_choice()
    print("Player 1 claims to choose", claim1.name)
    print("Player 2 claims to choose", claim2.name)
    # Choice
    move1 = player1.random_strategy(claim1)
    move2 = player1.random_strategy(claim2)
    print("Player 1 chooses", move1.name)
    print("Player 2 chooses", move2.name)
    # Result
    result = compare(move1, move2)
    if result == 0:
        print("Tie!")
    elif result == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
    # Update
    player1.update(claim1, move1, Result(result))
    player2.update(claim2, move2, Result(result * -1))
    print()

print(player1.get_all_stats())
print(player2.get_all_stats())