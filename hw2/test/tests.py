from hw2.src.num import *
from hw2.src.sym import *
import random
from hw2.src.data import *

def eg_sym():
    s = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(x)
    mode = s.mid()
    print(mode)
    return mode == "a"

def eg_num():
    e = NUM()
    for _ in range(1000):
        e.add(random.normalvariate(10, 2))
    mu = e.mid()
    print(mu)
    return 9.9 < mu < 10.1

def eg_csv():
    n = 0
    d = DATA('../../data/auto93.csv')

    return len(d.rows)-1 == 398

def run_all_tests():
  print(eg_sym())
  print(eg_num())
  print('all tests')

def run_tests(test_name):
  if (test_name=='all'):
    run_all_tests()
  elif (test_name=='sym'):
    print(eg_sym())
  elif (test_name=='num'):
     print(eg_num())
  elif (test_name=='csv'):
     print(eg_csv())
