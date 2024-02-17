from col import COLS
from row import ROW
import re,ast,fileinput
from hw5.config import *
from l import *
from node import *
import random

def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]


class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None  
        if isinstance(src, str):
            reader = csv(src)
            for row in reader:
                self.add(ROW(row), fun)
        else:
            for row in (src or []):
                self.add(ROW(row), fun)

    def add(self, row, fun=None):

        if self.cols is None:
            self.cols = COLS(row.cells)
        else:
            if fun is not None:
                fun(self, row)

            self.cols.add(row)

        self.rows.append(row)

    def mid(self, cols=None, hw4=True):
        # Calculate the mid (mean/mode) of the specified columns
        u = {}
        ans = []
        target_cols = {**self.cols.x, **self.cols.y} if cols is None else cols
        if hw4:
            for _,col in target_cols.items():
                ans.append(col.mid())
            ans.insert(2, 0)
            return ROW(ans)
        u[".N"] = len(self.rows)-1
        for _,col in target_cols.items():
            u[col.txt] = col.mid()
        return ROW(u)
    
    def clone(self, rows=None):
        new_data = DATA([self.cols.names])
        for row in (rows or []):
            new_data.add(row)
        return new_data
    
    def farapart(self, rows, sortp=False, a=None):
        far = int((len(rows)-1) * the.Far)
        evals = 1 if a else 2
        a = any_item(rows)
        a_neighbors = sorted(a.neighbors(self), key=lambda row: row.d2h(self))
        b = a_neighbors[far]

        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a

        return a, b, a.dist(b, self), evals
    
    def half(self, rows, sortp=True, before=None):
        some = random.sample(rows, min(the.Half, len(rows)))
        a, b, C, evals = self.farapart(some, sortp, before)
        as_ = []
        bs = []

        def project(r):
            return (r.dist(a, self) ** 2 + C ** 2 - r.dist(b, self) ** 2) / (2 * C)
        rows = rows[1:]
        sorted_rows = sorted(rows, key=project)
        midpoint = len(rows) // 2
        as_, bs = sorted_rows[:midpoint], sorted_rows[midpoint:]

        return as_, bs, a, b, C, a.dist(bs[0], self), evals

    # def tree(self, sortp=True):
    #     evals = 0

    #     def _tree(data, above=None):
    #         nonlocal evals
    #         node = NODE(data)
    #         if len(data.rows) > 2 * (len(self.rows) ** 0.5):
    #             lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
    #             evals += evals1
    #             node.lefts = _tree(self.clone(lefts))
    #             node.rights = _tree(self.clone(rights))
    #         return node

    #     return _tree(self), evals

    # def tree(self, sortp=True):
    #     evals=0
    #     def _tree(data, depth=0):
    #         if len(data.rows) <= 1:
    #             return {"data": data, "depth": depth}
    #         left_rows, right_rows = self.half(data.rows, sortp)
    #         left_data = data.clone(left_rows)
    #         right_data = data.clone(right_rows)
    #         return {
    #             "left": _tree(left_data, depth+1),
    #             "right": _tree(right_data, depth+1),
    #             "depth": depth
    #         }
        
    #     return _tree(self), evals

    def tree(self, sortp=True):
        evals = 0

        def _tree(data, above=None):
            nonlocal evals
            node = NODE(data)
            if len(data.rows) > 2 * math.sqrt(len(self.rows)):
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = data.half(data.rows, sortp, above)
                evals += evals1
                node.left = _tree(data.clone(lefts))
                node.right = _tree(data.clone(rights))
                print(node.left, node.right)
            return node

        root = _tree(self)
        return root, evals

    def branch(self, stop=2):
        def _branch(data, depth=0):
            if len(data.rows) <= stop:
                return {"data": data, "depth": depth}
            left_rows, right_rows = self.half(data.rows, True)
            left_data = data.clone(left_rows)
            return _branch(left_data, depth+1)
        
        return _branch(self)
