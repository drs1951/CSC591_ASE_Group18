from rule import *
from project_k_means.config import *
from l import *

class RULES:
    def __init__(self, ranges, goal, rowss):
        self.sorted = []
        self.goal = goal
        self.rowss = rowss
        self.LIKE = 0
        self.HATE = 0
        self.like_hate()
        for range in ranges:
            range.scored = self.score(range.y)
        self.sorted = self.top(self.try_(self.top(ranges)))

    def like_hate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE += len(rows)

    def score(self, t):
        return score(t, self.goal, self.LIKE, self.HATE)

    def try_(self, ranges):
        u = []
        for subset in powerset(ranges):  
            if subset:
                rule = RULE(subset)
                rule.scored = self.score(rule.selectss(self.rowss))
                if rule.scored > 0.01:
                    u.append(rule)
        return u

    def top(self, t):
        t.sort(key=lambda x: x.scored, reverse=True)
        u = [x for x in t if x.scored >= t[0].scored * the.Cut] 
        return u[:the.Beam]  
