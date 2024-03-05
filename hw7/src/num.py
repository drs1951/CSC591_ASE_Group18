import math

class NUM:
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
    
    def div(self):
        return math.sqrt(self.m2 / (self.n - 1)) if self.n >= 2 else 0
    
    def like(self, x, prior):
        x = float(x)
        mu, sd = self.mid(), self.div() + 1E-30
        nom = math.exp(-0.5 * (x - mu)**2 / sd**2)
        denom = sd * 2.5 + 1E-30
        return nom / denom
    
    def norm(self, x):
        if x == "?":
            return x
        else:
            x = float(x)
            return (x - self.lo) / (self.hi - self.lo + 1E-30)  # Adding a small constant to avoid division by zero