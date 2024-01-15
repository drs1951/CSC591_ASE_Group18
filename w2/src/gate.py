import math
import random
import argparse

# Assuming global settings are set somewhere in the code
the = {
    "cohen": 0.35,
    "k": 1,
    "m": 2,
    "seed": 31210
}

random.seed(the["seed"])

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

class COLS:
    def __init__(self, row_cells):
        self.x = {}
        self.y = {}
        self.all = []
        self.klass = None
        self.names = row_cells

        for at, txt in enumerate(row_cells):
            # If the column name is uppercase, use NUM, otherwise use SYM
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            # If column name does not end in 'X', add it to x or y
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = col
                # Add to y if it ends with '!', '+', or '-', otherwise add to x
                if any(txt.endswith(special) for special in ["!", "+", "-"]):
                    self.y[at] = col
                else:
                    self.x[at] = col

    def add(self, row):
        merged_x_y = {**self.x, **self.y}
        # Assuming row is an instance of ROW class and has a 'cells' attribute which is a list or dict
        for _,col in merged_x_y.items():
            value = row.cells[col.txt]  # Get the value from the row
            col.add(value)  # Use the 'add' method of NUM or SYM to add the value
        return row
class ROW:
    def __init__(self, cells):
        self.cells = cells

# # Example usage:
# # If 't' is a dictionary where keys are column names and values are the data for those columns:
# row_data = {"Name": "Alice", "Age": 30, "Score": 85.5}
# row = ROW(row_data)


import csv
import random

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None  # This will be an instance of COLS once initialized
        if isinstance(src, str):
            # If src is a string, treat it as a filename and read rows from the CSV
            with open(src, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row in reader:
                    self.add(ROW(row), fun)
        else:
            # If src is not a string, treat it as a list of rows
            for row in src:
                self.add(ROW(row), fun)

    def add(self, row, fun=None):
        # If cols is not yet initialized, do so with the first row
        # print(row.cells)
        if self.cols is None:
            self.cols = COLS(row.cells.keys())
            # print([x for x in self.cols.all ])
            
        else:
            # If fun is defined, call it before updating anything
            if fun is not None:
                fun(self, row)
            # Add the row to the cols
            # print("error her÷
            self.cols.add(row)
            
        # Add the row to the list of rows
        self.rows.append(row)

    def mid(self, cols=None):
        # Calculate the mid (e.g., mean) of the specified columns or all columns
        u = {}
        target_cols = {**self.cols.x, **self.cols.y} if cols is None else cols
        for _,col in target_cols.items():
            u[col.txt] = col.mid()
        return ROW(u)


# print(d.mid().cells)

parser = argparse.ArgumentParser()

parser.add_argument('--file', '-f', help = "file path", type = str)
args = parser.parse_args()
d = DATA(src = args.file)
print(d.mid().cells)
