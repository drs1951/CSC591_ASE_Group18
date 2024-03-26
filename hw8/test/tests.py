from hw8.src.data import *
from hw8.config import *
from hw8.src import l
from hw8.src.range import *
from hw8.src.rule import *
from hw8.src.rules import *
import random

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

def score_range(range_obj, like_count, hate_count):
    return range_obj.score("LIKE", like_count, hate_count)

def eg_bins():
    d = DATA("data/auto93.csv")
    best, rest, _ = d.branch()
    like = best.rows
    hate = rest.rows[:3 * len(like)] 

    ranges = []

    print("\nOutput 1:\n")
    for col in d.cols.x.values():
        for range_obj in ranges1(col, {'LIKE': like, 'HATE': hate}):
            range_obj.custom_print()
            ranges.append(range_obj)
    ranges.sort(key=lambda x: score_range(x, len(like), len(hate)), reverse=True)
    max_score = score_range(ranges[0], len(like), len(hate))

    print("\nOutput 2:\n")
    print("\n#scores:\n")
    for v in ranges:
        current_score = score_range(v, len(like), len(hate))
        if current_score > 0.1 * max_score:
            print(f"{current_score:.2f} ", end=' ')
            v.custom_print()

    print({'LIKE': len(like), 'HATE': len(hate)})

def eg_rules():
    for xxx in range(1, 2):  
        d = DATA(the.file)  
        
        best0, rest, evals1 = d.branch(the.d)
        best, _, evals2 = best0.branch(the.D)
        print(evals1 + evals2 + the.D - 1)
        
        LIKE = best.rows
        HATE = slice(shuffle(rest.rows), 1, 3 * len(LIKE))  
        rowss = {"LIKE": LIKE, "HATE": HATE}
        
        for i, rule in enumerate(RULES(ranges(d.cols.x, rowss), "LIKE", rowss).sorted):
            result = d.clone(rule.selects(rest.rows))
            if len(result.rows) > 0:
                result.rows.sort(key=lambda a: a.d2h(d))  
                print(l.rnd(rule.scored), 
                      l.rnd(result.mid().d2h(d)), 
                      l.rnd(result.rows[0].d2h(d)),
                      l.o(result.mid().cells), 
                      "\t", rule.show())  


def run_tests(d):
    # print("Cluster Output")
    # eg_tree()
    # print("\nOptimization Output")
    # print("\nSingle Descent Output")
    # eg_branch()
    # print("\nDouble Tap Output")
    # eg_doubletap()
    # eg_dist()
    # print()
    # print("Output of Far function")
    # eg_far()
    # print("Output of Bin function")
    # eg_bins()
    eg_rules()