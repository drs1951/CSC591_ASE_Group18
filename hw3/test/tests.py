import sys
import random
from hw3.src.num import *
from hw3.src.sym import *
from hw3.src.data import *
from hw3.config import *

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

def learn(data, row, my):
    my["n"] = my["n"] + 1
    kl = row.cells[data.cols.klass.at]
    if my["n"] > 10:
        my["tries"] = my["tries"] + 1
        my["acc"] = my["acc"] + (kl == row.likes(my["datas"])[0] and 1 or 0)
    my["datas"][kl] = my["datas"].get(kl, DATA(data.cols.names))
    my["datas"][kl].add(row)

def eg_bayes(src):
    wme = {"acc": 0, "datas": {}, "tries": 0, "n": 0}
    data = DATA(src=src, fun=lambda data, t: learn(data, t, wme))
    print(f"Accuracy of Naive Bayes Classifier: {(wme['acc'] / wme['tries'])}")
    return wme["acc"] / wme["tries"]
  
def diabetes():
  return eg_bayes("data/diabetes.csv") > 0.72

def soybean():
  for k in range(4):
    the.k = k
    for m in range(4):
      the.m = m
      eg_bayes("data/soybean.csv")

def run_all_tests():
  sym_result = eg_sym()
  num_result = eg_num()
  csv_result = eg_csv()
  diabetes_result = diabetes()
  soybean_result = soybean()

  print(f"\nSYM: {sym_result}")
  print(f"NUM: {num_result}")
  print(f"CSV: {csv_result}")
  print(f"Diabetes: {diabetes_result}")

  total_tests = 4
  passed_tests = sum([sym_result, num_result, csv_result, diabetes_result])
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
  elif (test_name=='naive_bayes'):
     print(eg_csv())
