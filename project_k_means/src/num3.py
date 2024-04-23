from project_k_means.config import *
import math

class NUM3:
    def __init__(self, txt="", at=0):
        self.txt = txt
        self.at = at
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if txt.endswith('-') else 1

    def add(self, x):
        if x != "?":
            x = float(x)
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)
    
    def mid(self):
        return round(self.mu,2)
    
    def norm(self, x):
        if x == "?":
            return x
        else:
            x = float(x)
            return (x - self.lo) / (self.hi - self.lo + 1E-30)  # Adding a small constant to avoid division by zero

    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1
        x, y = self.norm(x), self.norm(y)
        if x == "?":
            x = 1 if y < 0.5 else 0
        if y == "?":
            y = 1 if x < 0.5 else 0
        return abs(x - y)
    
    def bin(self, x):
        if self.hi == self.lo:
            return 1
        tmp = (self.hi - self.lo) / (the.bins - 1)
        return math.floor(x / tmp + .5) * tmp
