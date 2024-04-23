class SYM2:
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
    
    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1
        return 0 if x == y else 1
    
    def bin(self,x):
        return x