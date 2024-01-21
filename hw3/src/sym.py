import sys
sys.path.append("../CSC591_ASE_Group18/")
from hw2.config import *

class SYM:
    def __init__(self, txt="", at=0):
        self.txt = txt
        self.at = at
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = self.has.get(x, 0) + 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode
    
    def like(self, x, prior):
        return ((self.has.get(x, 0) or 0) + the["m"] * prior) / (self.n + the["m"])