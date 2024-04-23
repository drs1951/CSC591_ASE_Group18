import sys
sys.path.append("../CSC591_ASE_HW_Group12/")
import time
from project_rrp.src.data2 import *
from project_rrp import config
from project_rrp.src import l
from project_rrp.src.range import *
from project_rrp.src.rule import *
from project_rrp.src.rules import *
# import numpy as np
import random

def eg_dist():
    d = DATA2(src="data/auto93.csv")
    r1 = d.rows[1]  
    rows = r1.neighbors(d)

    for i, row in enumerate(rows, start=0):
        if i % 30 == 0:
            print(row.cells, round(r1.dist(row, d), 3))

def eg_far():
    d = DATA2(src = "data/auto93.csv")
    a, b, C, _ = d.farapart(d.rows)
    print(l.o(a))
    print(l.o(b))
    print(C)

def eg_tree(data_path, stop):
    # stop = 398
    t, data, evals = DATA2(data_path).tree(True, stop)
    return t.show(stop, data)
    # print(f"evals: {evals}")


def eg_branch():
    d = DATA2("data/auto93.csv")
    best, rest, evals = d.branch()
    print(best.mid().cells)
    print(f"evals: {evals}")

def eg_doubletap():
    d = DATA2("data/auto93.csv")
    best1, rest, evals1 = d.branch(20)
    # best2, _, evals2 = best1.branch(4)
    print()
    # print(best1.mid().cells, rest.mid().cells)
    # print(evals1 + evals1)

def score_range(range_obj, like_count, hate_count):
    return range_obj.score("LIKE", like_count, hate_count)

def eg_bins():
    d = DATA2("data/auto93.csv")
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
        d = DATA2(the.file)  
        
        best0, rest, evals1 = d.branch(the.d)
        best, _, evals2 = best0.branch(the.D)
        # print(f"Evals: {evals1 + evals2 + the.D - 1}")
        
        LIKE = best.rows
        HATE = slice(shuffle(rest.rows), 1, 3 * len(LIKE))
        rowss = {"LIKE": LIKE, "HATE": HATE}
        print()
        print("score", "\t\t\t" ,"mid selected", "\t\t\t\t\t", "rules")
        print("_____", "\t" ,"__________________________________________________", "\t", "__________________")
        print()
        for i, rule in enumerate(RULES(ranges(d.cols.x, rowss), "LIKE", rowss).sorted):
            result = d.clone(rule.selects(rest.rows))
            # result.rows = result.rows[1:] ek change
            result.rows = result.rows
            if len(result.rows) > 0:
                result.rows.sort(key=lambda a: a.d2h(d))  
                print(l.rnd(rule.scored), "\t",
                    #   l.rnd(result.mid().d2h(d)), 
                    #   l.rnd(result.rows[0].d2h(d)),
                      l.o(result.mid()),
                      "\t", rule.show())  

def run_rrp(data_path, stop):
    # print("in test")
    # print(config.the)
    list_d2h = []
    total_time = 0
    for i in range(20):
        random.seed(i*7+49)
        start_time = time.time()
        ans = eg_tree(data_path, stop)
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time
        # list_d2h.append(ans*1000)
        if 'xomo' in data_path or 'dtlz' in data_path:
            list_d2h.append(ans*1000)    
        else:
            list_d2h.append(ans)
    # average_time = total_time/20
    return [list_d2h, round(total_time/20,2)]

def run_rand(data_path, stop):
    d2h_list = []
    for i in range(20):
        random.seed(i*7+49)
        d = DATA2(data_path)
        sample = random.sample(d.rows, stop)
        dist = [x.d2h(d) for x in sample]
        if 'xomo' in data_path or 'dtlz' in data_path:
            d2h_list.append(min(dist)*1000)    
        else:
            d2h_list.append(min(dist))
    return d2h_list

def run_tests(d):
    # print("Cluster Output")
    eg_tree('data/auto93.csv', 20)
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
    # eg_rules()