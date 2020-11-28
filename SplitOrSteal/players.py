from player import Player
from mechanics import *

# Has equal chance of choosing split/steal
class RandomPlayer(Player):
    
    def __init__(self):
        super().__init__()
    
    def action(self):
        return self.random_action()


# Always split
class NicePlayer(Player):
    
    def __init__(self):
        super().__init__()
    
    def action(self):
        return self.split()


# Always steal
class GreedyPlayer(Player):
    
    def __init__(self):
        super().__init__()
    
    def action(self):
        return self.steal()


# Alternate between split and steal
# Initial choice is random
class FicklePlayer(Player):
    
    def __init__(self):
        super().__init__()
    
    def action(self):
        if self.round == 1:
            return self.random_action()
        else:
            if self.previous_actions[-1] == Move.SPLIT:
                return self.steal()
            else:
                return self.split()


# Always split, but once opponent steals, always steal
class GrudgePlayer(Player):
    
    def __init__(self):
        super().__init__()

    def action(self):
        if Result.SPLIT_LOST in self.previous_results:
            return self.steal()
        else:
            return self.split()


# Copy the previous move made by the opponent
# Initial choice is split
class CopycatPlayer(Player):
    
    def __init__(self):
        super().__init__()

    def action(self):
        if self.round == 1:
            return self.split()
        else:
            return self.opponent.previous_actions[-1]


# Split when winning, steal when losing
class SoreLoserPlayer(Player):

    def __init__(self):
        super().__init__()
    
    def action(self):
        if self.money >= self.opponent.money:
            return self.split()
        else:
            return self.steal()


# If opponent stole in the previous 2 rounds, steal
# Otherwise, always split
class CautiousPlayer(Player):
    
    def __init__(self):
        super().__init__()

    def action(self):
        if Move.STEAL in self.opponent.previous_actions[-2:]:
            return self.steal()
        else:
            return self.split()


# Always split, until the opponent steals twice
# Then becomes a CopycatPlayer
class CopykittenPlayer(Player):
    
    def __init__(self):
        super().__init__()
        self.limit = 2

    def action(self):
        if self.round == 1:
            return self.split()
        if self.opponent.previous_actions[-1] == Move.STEAL:
            self.limit -= 1
        if self.limit <= 0:
            return self.opponent.previous_actions[-1]
        else:
            return self.split()


# Starts with split, steal, split, split
# If opponent retaliates with steal, plays like a CopycatPlayer
# Otherwise, always steal
class StrategicPlayer(Player):

    def __init__(self):
        super().__init__()
    
    def action(self):
        if self.round == 1 or self.round == 3 or self.round == 4:
            return self.split()
        elif self.round == 2:
            return self.steal()
        elif Move.STEAL in self.opponent.previous_actions:
            return self.opponent.previous_actions[-1]
        else:
            return self.steal()