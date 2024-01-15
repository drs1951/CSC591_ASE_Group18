def t1():
  print('test1')

def run_all_tests():
  print('all tests')

def run_tests(test_name):
  if (test_name=='all'):
    run_all_tests()
  elif (test_name=='t1'):
    t1()