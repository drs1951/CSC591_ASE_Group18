from col import COLS
from row import ROW
import re,ast,fileinput
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
            # print(ROW(ans).cells)
            return ROW(ans)
        u[".N"] = len(self.rows)-1
        for _,col in target_cols.items():
            u[col.txt] = col.mid()
        return ROW(u)

    def gate(self, budget0, budget, some, ans):
        rows = self.rows[1:]
        rows = random.sample(rows, len(rows))
        # ans[0].append("1. top 6 \n " + str([top_6.cells[5:8] for top_6 in rows[:6]]))
        # ans[1].append("2. top 50 \n " + str([top_50.cells[5:8] for top_50 in rows[:50]]))
        # rows.sort(key=lambda x: x.d2h(self))
        # ans[2].append("3. most \n " + str(rows[0].cells[5:8]))
        # rows = random.sample(self.rows[1:], len(self.rows)-1)
        lite = rows[:budget0]
        dark = rows[budget0:]
        stats = []
        bests = []
        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            
            # print("4: rand", y values of centroid of (from DARK, select BUDGET0+i rows at random))
            # ans[3].append("4: rand \n " + str(self.get_centroid(random.sample(dark,budget0+i), 5, 8)))
            # ans[4].append("5: mid \n " + str(self.get_centroid(selected.rows[1:], 5, 8)))
            # ans[5].append("6: top: \n " + str(best.rows[1].cells[5:8]))
            stats.append(selected.mid())
            bests.append(best.rows[1])
            lite.append(dark.pop(todo))
        
        return stats, bests, lite

    def split(self, best, rest, lite, dark):
        selected = DATA([self.cols.names])
        max_val = 1E30
        out = 0

        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r:
                selected.add(row)
            tmp = abs(b + r) / abs(b - r + 1E-300)
            if tmp > max_val:
                out, max_val = i, tmp
        
        return out, selected

    def best_rest(self, rows, want):
        rows.sort(key=lambda x: x.d2h(self))
        best = [self.cols.names]
        rest = [self.cols.names]

        for i, row in enumerate(rows):
            (best if i < want else rest).append(row.cells)
        # print(best,rest)
        return DATA(best), DATA(rest)
      
    def get_centroid(self, rows, i, j):
      centroid = []
      for k in range(i,j):
        centroid.append(0)
      for row in rows:
        y = row.cells[i:j]
        centroid = [sum(k) for k in zip(y, centroid)]
      for k in range(len(centroid)):
        centroid[k]/=len(rows)
      return centroid
