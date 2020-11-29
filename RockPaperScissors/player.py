import random
from abc import ABC
from mechanics import *

# Abstract class for a Player
class Player(ABC):
    
    def __init__(self):
        super().__init__()
        # Initial
        self.reset()

    # Equal chance of picking ROCK, PAPER or SCISSORS
    def random_choice(self):
        return Move(random.randint(1,3))
    
    # Equal chance of using a random strategy
    def random_strategy(self, claim):
        roll = random.randint(0,2)
        if roll == 0:
            return self.step0_strategy(claim)
        elif roll == 1:
            return self.step1_strategy(claim)
        else:
            return self.step2_strategy(claim)
    
    # For claiming
    def choose_rock(self):
        return Move.ROCK
    
    def choose_paper(self):
        return Move.PAPER
    
    def choose_scissors(self):
        return Move.SCISSORS
    
    # Player chooses what player claimed
    def step0_strategy(self, claim):
        return claim

    # Player chooses one that can beat what the opponent will choose,
    # assuming that the opponent believes the player is honest
    def step1_strategy(self, claim):
        return Move(MATCHUP[claim.value])

    # Player chooses one that can beat what the opponent will choose,
    # assuming that the opponent believes that the player is using step1 strategy
    def step2_strategy(self, claim):
        return Move(list(MATCHUP.keys())[list(MATCHUP.values()).index(claim.value)])
    
    def update(self, claim, choice, result):
        self.results[result.name] += 1
        self.previous_claims.append(claim)
        self.previous_choices.append(choice)
        self.previous_strategies.append(Strategy(compare(claim, choice)))
        self.previous_results.append(result)
        self.update_honesty(claim, choice)
        self.round += 1
    
    def observe(self, opponent):
        self.opponent = opponent
    
    # A: 80-100% honest
    # B: 60-79% honest
    # C: 40-59% honest
    # D: 20-39% honest
    # E: 0-19% honest
    def update_honesty(self, claim, choice):
        if claim == choice:
            self.honest_count += 1
        honest_percent = (self.honest_count * 100) / len(self.previous_claims)
        if honest_percent >= 80:
            self.honesty = 'A'
        elif honest_percent >= 60:
            self.honesty = 'B'
        elif honest_percent >= 40:
            self.honesty = 'C'
        elif honest_percent >= 20:
            self.honesty = 'D'
        else:
            self.honesty = 'E'
    
    def reset(self):
        self.round = 1
        self.results = {'WIN': 0, 'TIE': 0, 'LOSE': 0}
        self.honest_count = 0
        self.honesty = 'A'
        # Save history
        self.previous_claims = []
        self.previous_choices = []
        self.previous_strategies = []
        self.previous_results = []
        # Save state of opponent
        self.opponent = None
    
    def get_class(self):
        return self.__class__.__name__
    
    def get_all_stats(self):
        return {'Rounds': self.round,
                'Results': self.results,
                'Honesty': self.honesty,
                'Claims': [c.name for c in self.previous_claims],
                'Choices': [c.name for c in self.previous_choices],
                'Strategies': [s.name for s in self.previous_strategies],
                'Win History': [r.name for r in self.previous_results]
               }