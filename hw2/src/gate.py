import sys
from tests import run_tests
import random
from data import DATA

the = {
    "cohen": 0.35,
    "k": 1,
    "m": 2,
    "seed": 31210
}

random.seed(the["seed"])

def get_stats(file):
  data = DATA(src = file)
  print(data.mid().cells)
  
def help():
    print("OPTIONS:")
    print("  -h --help     show help                       = false")
    print("  -f --file     csv data file name              = ../../data/auto93.csv")
    print("  -t --todo     todo an action command          = todo")
    print("  -c --cohen    small effect size               = .35")
    print("  -k --k        low class frequency kludge      = 1")
    print("  -m --m        low attribute frequency kludge  = 2")
    print("  -s --seed     random number seed              = 31210")
    sys.exit(0)
  
def arg_parser(argv):
  args = {}
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