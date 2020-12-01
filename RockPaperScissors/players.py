import random
from player import Player

# Random claim
# Random choice
class RandomPlayer(Player):

    def __init__(self):
        super().__init__()


# Random claim
# Honesty level never goes below A (80%)
class HonestPlayer(Player):

    def __init__(self):
        super().__init__()
    
    def choose(self, claim):
        # Check honesty level if the player were to lie this round
        honest_percent = self.honest_count / (len(self.previous_claims) + 1)
        # If honesty would go below A, never lie
        if honest_percent < 0.8:
            return self.step0_strategy(claim)
        # Otherwise, has 50% chance to lie
        else:
            roll = random.randint(0,4)
            if roll <= 1:
                return self.step0_strategy(claim)
            elif roll == 2:
                return self.step1_strategy(claim)
            else:
                return self.step2_strategy(claim)


# Random claim
# Honesty level never goes above E (20%)
class DishonestPlayer(Player):

    def __init__(self):
        super().__init__()
    
    def choose(self, claim):
        # Check honesty level if the player were to not lie this round
        honest_percent = (self.honest_count + 1) / (len(self.previous_claims) + 1)
        # If honesty would go above E, lie
        if honest_percent > 0.2:
            roll = random.randint(0, 1)
            if roll == 0:
                return self.step1_strategy(claim)
            else:
                return self.step2_strategy(claim)
        # Otherwise, has 50% chance to lie
        else:
            roll = random.randint(0,4)
            if roll <= 1:
                return self.step0_strategy(claim)
            elif roll == 2:
                return self.step1_strategy(claim)
            else:
                return self.step2_strategy(claim)