from hw2.src.num import *
from hw2.src.sym import *

def eg_sym():
    s = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(x)
    mode = s.mid()
    print(mode)
    return mode == "a"

def run_all_tests():
  print(eg_sym())
  print('all tests')

def run_tests(test_name):
  if (test_name=='all'):
    run_all_tests()
  elif (test_name=='sym'):
    print(eg_sym())