from num import *
from sym import *

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