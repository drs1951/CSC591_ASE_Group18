from project_k_means.config import *

class ROW3:
    def __init__(self, cells):
        self.cells = cells

    def d2h(self, data, p=2):
        d, n = 0, 0
        for col in data.cols.y.values():
            x = self.cells[col.at]
            if x is None:
                print("?", end="")
            else:
                n += 1
                d += abs(col.heaven - col.norm(self.cells[col.at])) ** p
        return (d / n) ** (1 / p) if n > 0 else 0

    def dist(self, other, data, p=None):
        if p is None:
            p = the.p 
        d, n = 0, 0
        for col in data.cols.x.values():
            n += 1
            d += col.dist(self.cells[col.at], other.cells[col.at]) ** p
        return (d / n) ** (1 / p) if n > 0 else 0

    def neighbors(self, data, rows=None):
        rows = rows if rows is not None else data.rows[1:]
        return sorted(rows, key=lambda row: self.dist(row, data))