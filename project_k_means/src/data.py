from col import COLS
from row import ROW
import re,ast,fileinput
from project_k_means.config import *
from l import *
from node import *
import random
from sklearn.cluster import KMeans
import numpy as np

def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]


class DATA:
    def __init__(self, src, fun=None, isListOFRows=False):
        self.rows = []
        self.cols = None  
        if isinstance(src, str):
            reader = csv(src)
            for row in reader:
                self.add(ROW(row), fun)
        elif isListOFRows:
            for row in src:
                self.add(row)
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

    def tree(self, sortp=True, stop=0):
        evals = 0
        # self.rows = self.rows[1:]

        def _tree(data, stop, above=None):
            nonlocal evals
            node = NODE(data)
            
            if len(data.rows) > 2 * stop:
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = data.half(data.rows, sortp, above)
                evals += evals1
                node.lefts = _tree(data.clone(lefts), stop)
                node.rights = _tree(data.clone(rights), stop)
            return node

        root = _tree(self, stop)
        return root, evals

    def branch(self, stop=None):
        evals = 1
        rest = []

        stop = stop or (2 * len(self.rows) ** 0.5)

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals
            if len(data.rows) > stop:
                lefts, rights, left, b, C, dis_a_to_bs, _ = data.half(data.rows[1:], True, above)
                evals += 1
                rest.extend(rights)
                return _branch(data.clone(lefts), left)
            else:
                return data.clone(data.rows[1:]), data.clone(rest), evals

        return _branch(self)


    def k_means(self,k, stop):
        for row in self.rows[1:]:
            for index,vl in enumerate(row.cells):
                if vl == '?':
                    row.cells[index] = self.cols.all[index].mid()

        X = np.array([np.array(row.cells) for row in self.rows[1:]])
        kmeans = KMeans(n_clusters = k, n_init = 100).fit(X)
        centroids =  [ROW(cluster).d2h(self) for cluster in kmeans.cluster_centers_]
        
        sorted_centroids = sorted(centroids)
        total_points = []
        idx = 0
        while (len(total_points) < stop):
            mn_d2h_cluster_index = centroids.index(sorted_centroids[idx])
            idx+=1
            centroids_points = list(X[kmeans.labels_ == mn_d2h_cluster_index])
            if len(centroids_points) > stop-len(total_points):
                sorted_centroid_points = sorted(centroids_points, key = lambda x:ROW(x).d2h(self))
                # sorted_centroid_points = [ROW(point).d2h(self) for point in centroids_points]
                total_points.extend(sorted_centroid_points[:stop-len(total_points)])
            else:
                total_points.extend(centroids_points)
        total_points = [ROW(pt) for pt in total_points]
        return total_points