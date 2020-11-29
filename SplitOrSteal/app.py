import random
from players import *
from game import start_game

player_list = [RandomPlayer(), NicePlayer(), GreedyPlayer(), FicklePlayer(), GrudgePlayer(), \
               CopycatPlayer(), SoreLoserPlayer(), CautiousPlayer(), CopykittenPlayer(), StrategicPlayer()]

# Create players
user = Player()
opponent = random.choice(player_list)

# Initial configurations
pot = 1000
pool = 100
max_round = 10
print("Initial pot money:\t{}".format(pot))
print("Pool per round:\t{}".format(pool))
print("Maximum round:\t{}".format(max_round))
print()

# Start game
start_game(user, opponent, pot, pool, max_round)