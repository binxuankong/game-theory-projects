import random
from player import Player
from game import start_game

# Create players
user = Player()
opponent = Player()

# Initial configurations
rounds = 10

# Start game
start_game(user, opponent, rounds)