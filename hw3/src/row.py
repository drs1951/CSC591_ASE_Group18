import sys
sys.path.append("../CSC591_ASE_Group18/")
from hw3.config import *
import math 

class ROW:
    def __init__(self, cells):
        self.cells = cells

    def like(self, data, n, n_hypotheses):
        prior = (len(data.rows) + the["k"]) / (n + the["k"] * n_hypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)
        return math.exp(out)
    
    def likes(self, datas):
        n, n_hypotheses = 0, 0

        for data in datas:
            n += len(datas[data].rows)
            n_hypotheses += 1

        most, out = None, None

        for k, data in datas.items():
            tmp = self.like(datas[k], n, n_hypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most