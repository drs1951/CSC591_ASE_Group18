import sys
import random
sys.path.append("../../CSC591_ASE_Group18/")
from hw2.src.num import *
from hw2.src.sym import *
from hw2.src.data import *

def eg_sym():
    s = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(x)
    mode = s.mid()
    return mode == "a"

def eg_num():
    e = NUM()
    for _ in range(1000):
        e.add(random.normalvariate(10, 2))
    mu = e.mid()
    return 9.9 < mu < 10.1

def eg_csv():
    d = DATA('data/auto93.csv')
    return len(d.rows)-1 == 398

def run_all_tests():
  sym_result = eg_sym()
  num_result = eg_num()
  csv_result = eg_csv()

  print(f"\nSYM: {sym_result}")
  print(f"NUM: {num_result}")
  print(f"CSV: {csv_result}")

  total_tests = 3
  passed_tests = sum([sym_result, num_result, csv_result])
  print(f"\nPassed {passed_tests} out of {total_tests} tests.")
  print('All tests finished running.\n')

def run_tests(test_name):
  if (test_name=='all'):
    run_all_tests()
  elif (test_name=='sym'):
    print(eg_sym())
  elif (test_name=='num'):
     print(eg_num())
  elif (test_name=='csv'):
     print(eg_csv())
