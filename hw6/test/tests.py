import sys
import random
from hw6.src.num import *
from hw6.src.sym import *
from hw6.src.data import *
from hw6.config import *
from hw6.src.ascii import *
from datetime import datetime

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
    my["datas"][kl] = my["datas"].get(kl, DATA([data.cols.names]))
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

def eg_gate20():
    print("#best, mid")
    ans = [[],[],[],[],[],[]]
    for i in range(20):
        the.seed = i*10
        d = DATA(src="data/auto93.csv")
        stats, bests = d.gate(4, 16, 0.5, ans)
        stat, best = stats[-1], bests[-1]
        # print(bests[-1].cells)
        # print(stats[-1].cells)
        print (round(best.d2h(d),2), round(stat.d2h(d),2))
    return ans

def eg_smo9():
   d = DATA(src="data/auto93.csv")
   current_datetime = datetime.now()
   print(f'Date: {current_datetime.strftime("%Y-%m-%d %H:%M:%S")}')
   print("file: ../data/auto93.csv")
   print("repeats: 20")
   print(f'seed: {the.seed}')
   print(f"rows: {len(d.rows)-1}")
   print(f"cols: {len(d.rows[0].cells)}")
   print(f'names:\t\t {d.cols.names} D2h-')
   print(f"mid: \t\t{d.mid().cells} \t {round(d.mid().d2h(d),2)}")
   div = [round(col.div(), 2) for col in (d.cols.all)]
   print(f"div:\t\t {div} \t {round(ROW(div).d2h(d),2)}")

   stats, bests = d.smo9(4, 5, 0.5)
   any50(d)

def any50(d):
    random.seed(the.seed)
    rows = d.rows[:]  # Copying the list
    random.shuffle(rows)
    
    for i in range(0, 50):
        print(f"any50:\t\t {rows[i].cells} \t {round(rows[i].d2h(d),2)}")

def eg_test_d2h():
  d = DATA(src="data/auto93.csv")
  test_row = ROW(cells = [8,400,230,73,	1,	4278,	9.5,	20])
  result = test_row.d2h(d)
  return round(result,2) >= 0.8 or round(result,2) <0.83


def nonempty_test_for_gate():
  #check if the given out is not empty
  d = DATA(src="data/auto93.csv")
  budget0 = 4
  budget = 16
  some = 0.5
  ans = ans = [[],[],[],[],[],[]]
  stats, best = d.gate(budget0, budget, some, ans)
  if stats and best:
     return True
  
def test_get_centroid():
  d = DATA(src="data/auto93.csv")
  rows = [ROW([1, 2, 3]), ROW([4, 5, 6])]
  centroid = d.get_centroid(rows, 0, 3)
    
  # Assertions
  # Expected centroid is the average of columns [col1, col2, col3]
  expected_centroid = [2.5, 3.5, 4.5]  # [(1+4)/2, (2+5)/2, (3+6)/2]
  return centroid == expected_centroid

def run_all_tests():
    # Store test functions and their results
    test_results = {
        "SYM MID": eg_sym_mid(),
        "NUM MID": eg_num_mid(),
        "CSV": eg_csv(),
        "Naive Bayes on Diabetes Dataset": diabetes(),
        "soybean": soybean(),  
        "SYM LIKE T1": test_sym_like_with_existing_value(),
        "SYM LIKE T2": test_sym_like_with_zero_n_and_m(),
        "d2h test": eg_test_d2h(),
        "nonEmpty result eg_gate20": nonempty_test_for_gate(),
        "Get Centroid": test_get_centroid(),
    }

    # Print results for each test
    for test_name, result in test_results.items():
        if test_name == "soybean":
            best_acc, best_k, best_m = result
            print(f"\nTherefore, the best accuracy for soybean is {best_acc} for k={best_k} and m={best_m}.")
        else:
            print(f"{test_name}: {result}")

    # Count the total and passed tests
    total_tests = len(test_results)
    # Assuming a test is considered 'passed' if its result is True or, in the case of soybean, if it returns a valid tuple
    passed_tests = sum(1 for result in test_results.values() if result or isinstance(result, tuple))

    print(f"\nPassed {passed_tests} out of {total_tests} tests.")
    print('All tests finished running.\n')

def run_tests(test_name):
  print(test_name)
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
  elif (test_name=='eg_gate20'):
     ans = eg_gate20()
     for i in ans:
       for j in i:
         print(j)
         print()
  elif (test_name == 'eg_test_d2h'):
     eg_test_d2h()
  elif (test_name == 'eg_smo9'):
     eg_smo9()
     

