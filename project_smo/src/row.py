import sys
from project_smo.config import *
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
                if inc!=0:
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
    
    def d2h(self, data):
        d = 0
        n = 0
        # print(self.cells)
        for col_name,col in data.cols.y.items():
            # print(type(col_name))
            n += 1
            # d+= abs(col.heaven - col.norm(self.cells[data.cols.names[col_name]])) ** 2
            d += math.pow(math.fabs(data.cols.y[col_name].heaven - data.cols.y[col_name].norm(self.cells[col_name])), 2)
        return math.sqrt(d / n) if n > 0 else 0