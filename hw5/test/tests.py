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

def eg_tree():
    t, evals = DATA("data/auto93.csv").tree(True)
    t.show()
    print(f"evals: {evals}")

def eg_branch():
    d = DATA("data/auto93.csv")
    best, rest, evals = d.branch()
    print(best.mid().cells)
    print(f"evals: {evals}")

def eg_doubletap():
    d = DATA("data/auto93.csv")
    best1, rest, evals1 = d.branch(32)
    best2, _, evals2 = best1.branch(4)
    print(best2.mid().cells, rest.mid().cells)
    print(evals1 + evals2)

def run_tests(d):
    print("Cluster Output")
    eg_tree()
    print("\nOptimization Output")
    print("\nSingle Descent Output")
    eg_branch()
    print("\nDouble Tap Output")
    eg_doubletap()
    # eg_dist()
    # print()
    # print("Output of Far function")
    # eg_far()
