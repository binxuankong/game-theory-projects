import random
from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Strategy(Enum):
    STEP0 = 0
    STEP1 = 1
    STEP2 = -1

class Result(Enum):
    WIN = 1
    TIE = 0
    LOSE = -1

# ROCK beats SCISSORS; PAPER beats ROCK; SCISSORS beat PAPER
MATCHUP = {1: 3, 2: 1, 3: 2}

# Return 1 if move1 wins, 0, if tie, -1 if move2 wins
def compare(move1, move2):
    if move1 == move2:
        return 0
    elif MATCHUP[move1.value] == move2.value:
        return 1
    else:
        return -1