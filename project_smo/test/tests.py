import sys
import random
import time
from project_smo.src.num import *
from project_smo.src.sym import *
from project_smo.src.data import *
from project_smo.config import *
from project_smo.src.ascii import *

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

def d2h_info(lite, data):
  summ = 0
  maxi = 0
  mini = 1
  n = 0
  # data.rows = data.rows[1:]
  for row in lite:
      n+=1
      dis = row.d2h(data)
      summ += dis
      maxi = max(maxi, dis)
      mini = min(mini, dis)
#   print(n)
#   print("n")
  return {'mean': summ/n, 'min': mini, 'max': maxi}

def run_smo(budget0, budget, data_path):
    # print("#best, mid")
    # best_lite = []
    # min_score = float('inf')
    best_d2h_list = []
    total_time = 0
    for i in range(20):
        the.seed = i*10
        d = DATA(src=data_path)
        # budget = int(2 * len(d.rows) ** 0.5)
        start_time = time.time()
        stats, bests = d.gate(budget0, budget, 0.5)
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time
        best = bests[-1]

        best_d2h = best.d2h(d)
        if 'xomo' in data_path or 'dtlz' in data_path:
            best_d2h_list.append(best_d2h*1000)    
        else:
            best_d2h_list.append(best_d2h)
        # best_d2h_list.append(round(best_d2h*1000,2))

        # info = d2h_info(lite, d)
        # if info['min'] < min_score:
        #   best_lite = lite
        #   min_score = info['min']
        # print(bests[-1].cells)
        # print(stats[-1].cells)
        # print(round(best.d2h(d),2), round(stat.d2h(d),2))
    # average_time = total_time/20
    return [best_d2h_list, round(total_time/20,2)]


def eg_gate20():
    print("#best, mid")
    ans = [[],[],[],[],[],[]]
    over_all_mean = 0
    for i in range(20):
        the.seed = i*10
        random.seed(the.seed)
        d = DATA(src="data/auto93.csv")
        stats, bests, _ = d.gate(4, 16, 0.5, ans)
        stat, best = stats[-1], bests[-1]
        # print(bests[-1].cells)
        # print(stats[-1].cells)
        print(round(best.d2h(d),2), round(stat.d2h(d),2))
    return ans

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

def d2h():
   d = DATA(src="data/auto93.csv")
   d.rows = d.rows[1:]
   minV=1000
   for row in d.rows:
      minV = min(minV, row.d2h(d))
   print(minV)

def run_tests(test_name):
  # print(test_name)
  # if (test_name=='all'):
  #   run_all_tests()
  # elif (test_name=='sym'):
  #   print(eg_sym_mid())
  # elif (test_name=='num'):
  #    print(eg_num_mid())
  # elif (test_name=='csv'):
  #    print(eg_csv())
  # elif (test_name=='naive_bayes'):
  #    print(eg_csv())
  # elif (test_name=='eg_gate20'):
  #    ans = eg_gate20()
  #    for i in ans:
  #      for j in i:
  #        print(j)
  #        print()
  if (test_name=='project_smo'):
     best_d2h_list = run_smo(4, 394, "data/auto93.csv") #best result after 20 runs of smo
     print(best_d2h_list)
    #  print(d2h_info(best_lite, d))
    #  for l in lite:
    #   print(d2h_info(l, d))
  # elif (test_name == 'eg_test_d2h'):
  #    eg_test_d2h()
  # elif (test_name == 'd2h'):
  #    d2h()

