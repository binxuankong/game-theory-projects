import random
from abc import ABC
from mechanics import Move

# Abstract class for a Player
class Player(ABC):
    
    def __init__(self):
        super().__init__()
        # Initial
        self.round = 1
        self.money = 0
        # Save history
        self.previous_actions = []
        self.previous_results = []
        self.previous_earnings = []
        # Save state of opponent
        self.opponent = None
    
    def split(self):
        return Move.SPLIT
        
    def steal(self):
        return Move.STEAL
    
    def random_action(self):
        if random.uniform(0,1) > 0.5:
            return Move.SPLIT
        else:
            return Move.STEAL

    
    def update(self, choice, result, money):
        self.round += 1
        self.money += money
        self.previous_actions.append(choice)
        self.previous_results.append(result)
        self.previous_earnings.append(money)
    
    def observe(self, opponent):
        self.opponent = opponent
    
    def reset(self):
        self.round = 1
        self.money = 0
        self.previous_actions = []
        self.previous_results = []
        self.previous_earnings = []
        self.opponent = None