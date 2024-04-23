import sys
import random
sys.path.append("../CSC591_ASE_HW_Group12/")
from project_smo.test.tests import *
from project_smo.config import *
from data import DATA

# the = {
#     "cohen": 0.35,
#     "k": 1,
#     "m": 2,
#     "seed": 31210
# }

random.seed(the.seed)

def get_stats(file):
  data = DATA(src = file)
  print(data.mid().cells)
  
def help():
  helper_string = """
  OPTIONS:
    -h --help     show help                       = false
    -f --file     csv data file name              = data/auto93.csv
    -t --todo     todo an action command          = todo
    -c --cohen    small effect size               = .35
    -k --k        low class frequency kludge      = 1
    -m --m        low attribute frequency kludge  = 2
    -s --seed     random number seed              = 31210
  """
  print(helper_string)
  sys.exit(0)
  
def arg_parser(argv):
  args = {'todo': None, 'file': None}
  for i in range(1, len(argv), 2):
    if argv[i]=='-h' or argv[i]=='--help':
      help()
    if argv[i]=='-f' or argv[i]=='--file':
      args['file'] = argv[i+1]
    elif argv[i]=='-t' or argv[i]=='--todo':
      args['todo'] = argv[i+1]
  
  return args

def main():
    args = arg_parser(sys.argv)
        
    if (args['todo']=='stats'):
      get_stats(args['file'])
    else:
      run_tests(args['todo'])
    
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()