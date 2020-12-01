import random
from players import *
from game import start_game

player_list = [RandomPlayer(), HonestPlayer(), DishonestPlayer()]

# Create players
user = Player()
opponent = random.choice(player_list)

# Initial configurations
rounds = 10

# Start game
start_game(user, opponent, rounds)