import math
import l
from project_rrp.config import *

class Range:
    def __init__(self, at, txt, lo, hi=None):
        self.at = at
        self.txt = txt
        self.scored = 0
        self.x = {'lo': lo, 'hi': hi if hi is not None else lo}
        self.y = {}

    def add(self, x, y):
        
        self.x['lo'] = min(self.x['lo'], x)
        self.x['hi'] = max(self.x['hi'], x)
        self.y[y] = self.y.get(y, 0) + 1

    def show(self):
        lo, hi, s = self.x['lo'], self.x['hi'], self.txt
        if lo == -math.inf: return f"{s} < {hi}"
        if hi == math.inf: return f"{s} >= {lo}"
        if lo == hi: return f"{s} == {lo}"
        return f"{lo} <= {s} < {hi}"

    def score(self, goal, LIKE, HATE):
        return l.score(self.y, goal, LIKE, HATE)

    def merge(self, other):
        both = Range(self.at, self.txt, min(self.x['lo'], other.x['lo']))
        both.x['hi'] = max(self.x['hi'], other.x['hi'])
        for k, v in self.y.items():
            both.y[k] = v
        for k, v in other.y.items():
            both.y[k] = both.y.get(k, 0) + v
        return both

    def merged(self, other, tooFew):
        both = self.merge(other)
        e1, n1 = l.entropy(self.y)
        e2, n2 = l.entropy(other.y)
        if n1 <= tooFew or n2 <= tooFew:
            return both
        if l.entropy(both.y)[0] <= (n1 * e1 + n2 * e2) / (n1 + n2):
            return both
        
    def custom_print(self):
        print("{" +
              f"at: {self.at}, " +
              f"scored: {self.scored}, " +
              f"txt: {self.txt}, " +
              f"x: {{hi: {self.x['hi']}, lo: {self.x['lo']}}}, " +
              f"y: {self.y}" +
              "}")
        
def ranges(cols, rowss):
    t = []
    for col in cols.values():
        for range in ranges1(col, rowss):
            t.append(range)
    return t

def ranges1(col, rowss):
    out, nrows = {}, 0
    for y, rows in rowss.items():
        # rows=rows[1:] ek change
        nrows += len(rows)
        for row in rows:
            x = row.cells[col.at]
            if x != "?":
                bin = col.bin(x)
                if bin not in out:
                    out[bin] = Range(col.at, col.txt, x)
                out[bin].add(x, y)
    out = list(out.values())
    out.sort(key=lambda a: a.x['lo'])
    if hasattr(col,'has'):
        return out
    else:
        return _mergeds(out, nrows / the.bins)

def _mergeds(ranges, tooFew):
    i, t = 0, []
    while i < len(ranges):
        a = ranges[i]
        if i < len(ranges) - 1:
            both = a.merged(ranges[i + 1], tooFew)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1
    if len(t) < len(ranges):
        return _mergeds(t, tooFew)
    for i in range(1, len(t)):
        t[i].x['lo'] = t[i - 1].x['hi']
    t[0].x['lo'] = float('-inf')
    t[-1].x['hi'] = float('inf')
    return t