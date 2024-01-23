import sys
import random
from hw3.src.num import *
from hw3.src.sym import *
from hw3.src.data import *
from hw3.config import *
from hw3.src.ascii import *

def eg_sym_mid():
    s = SYM()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        s.add(x)
    mode = s.mid()
    return mode == "a"

def eg_num_mid():
    e = NUM()
    for _ in range(1000):
        e.add(random.normalvariate(10, 2))
    mu = e.mid()
    return 9.9 < mu < 10.1

def eg_csv():
    d = DATA('data/auto93.csv')
    return len(d.rows)-1 == 398

def test_sym_like_with_existing_value():
    s = SYM()
    s.add("Existing")
    result = s.like("Existing", 0.5)
    expected = (s.has["Existing"] + the["m"] * 0.5) / (s.n + the["m"])
    return result==expected

def test_sym_like_with_zero_n_and_m():
    # Setting n and m to zero
    s = SYM()
    s.n = 0
    the["m"] = 0
    result = s.like("SomeValue", 0.5)
    return result== the["m"] * 0.5

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
    print(f"For k={the.k} and m={the.m}: {(wme['acc'] / wme['tries'])}")
    return wme["acc"] / wme["tries"]
  
def diabetes():
  print("\nAccuracy of Naive Bayes Classifier on Diabetes Dataset:")
  return eg_bayes("data/diabetes.csv") > 0.72

def soybean():
  best_acc,best_k,best_m=0,0,0
  print("\nAccuracy of Naive Bayes Classifier on Soybean Dataset:")
  for k in range(4):
    the.k = k
    for m in range(4):
      the.m = m
      current_acc = eg_bayes("data/soybean.csv")
      if current_acc > best_acc:
                best_acc = current_acc
                best_k = k
                best_m = m
  return best_acc,best_k,best_m


def run_all_tests():
  sym_mid_result = eg_sym_mid()
  num_mid_result = eg_num_mid()
  csv_result = eg_csv()
  diabetes_result = diabetes()
  best_acc,best_k, best_m = soybean()
  sym_like_1=test_sym_like_with_existing_value()
  sym_like_2=test_sym_like_with_zero_n_and_m()

  print(f"\nTherefore, the best accuracy for soybean is {best_acc} for k={best_k} and m={best_m}.")
  display()


  print(f"\nSYM MID: {sym_mid_result}")
  print(f"NUM MID: {sym_mid_result}")
  print(f"CSV: {csv_result}")
  print(f"SYM LIKE T1: {sym_like_1}")
  print(f"SYM LIKE T2: {sym_like_2}")
  print(f"Naive Bayes on Diabetes Dataset: {diabetes_result}")

  total_tests = 4
  passed_tests = sum([sym_mid_result, num_mid_result, csv_result, diabetes_result])
  print(f"\nPassed {passed_tests} out of {total_tests} tests.")
  print('All tests finished running.\n')

def run_tests(test_name):
  if (test_name=='all'):
    run_all_tests()
  elif (test_name=='sym'):
    print(eg_sym_mid())
  elif (test_name=='num'):
     print(eg_num_mid())
  elif (test_name=='csv'):
     print(eg_csv())
  elif (test_name=='naive_bayes'):
     print(eg_csv())
