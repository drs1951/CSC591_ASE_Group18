import math
import random
import argparse
from num import NUM
from sym import SYM
from col import COLS
from row import ROW
from tests import run_tests

# Assuming global settings are set somewhere in the code
the = {
    "cohen": 0.35,
    "k": 1,
    "m": 2,
    "seed": 31210
}

random.seed(the["seed"])

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
      
def get_stats(data):
  print(data.mid().cells)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', '-f', help = "file path", type = str)
    parser.add_argument('--todo', '-t', help = "action that need to be performed", type = str)
    args = parser.parse_args()
    data = DATA(src = args.file)
    if (args.todo=='stats'):
      get_stats(data)
    else:
      run_tests(args.todo)
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()