from hw5.src.data import *
from hw5.config import *
from hw5.src import l

def eg_dist():
    d = DATA(src="data/auto93.csv")
    r1 = d.rows[1]  
    rows = r1.neighbors(d)

    for i, row in enumerate(rows, start=0):
        if i % 30 == 0:
            print(row.cells, round(r1.dist(row, d), 3))

def eg_far():
    
    d = DATA(src = "data/auto93.csv")
    a, b, C, _ = d.farapart(d.rows)
    print(l.o(a))
    print(l.o(b))
    print(C)

# def eg_tree():
#     data, evals = DATA("data/auto93.csv").tree(True)
#     data.show()
#     print(evals)

def run_tests(d):
    print("Output of distance function")
    eg_dist()
    print()
    print("Output of Far function")
    eg_far()
