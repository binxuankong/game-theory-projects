import random
from enum import Enum

class Move(Enum):
    SPLIT = 0
    STEAL = 1

class Result(Enum):
    SPLIT_WON = 0
    SPLIT_LOST = 1
    STOLE_WON = 2
    STOLE_LOST = 3