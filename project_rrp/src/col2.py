from num2 import *
from sym2 import *

class COLS2:
    def __init__(self, row_cells):
        self.x = {}
        self.y = {}
        self.all = []
        self.klass = None
        self.names = row_cells

        for at, txt in enumerate(row_cells):

            col = NUM2(txt, at) if txt[0].isupper() else SYM2(txt, at)
            self.all.append(col)

            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = col

                if any(txt.endswith(special) for special in ["!", "+", "-"]):
                    self.y[at] = col
                else:
                    self.x[at] = col

    def add(self, row):
        merged_x_y = {**self.x, **self.y}

        for _,col in merged_x_y.items():
            value = row.cells[col.at]
            # print(row.cells)
            col.add(value) 
        return row