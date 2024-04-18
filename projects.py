import sys
sys.path.append("../CSC591_ASE_HW_Group12/")
from raise_utils.interpret import ScottKnott
# sys.path.append('../CSC591_ASE_HW_Group12/project_rrp/src')
# from project_rrp.test.tests import *
# from project_smo.test.tests import *
# from project_k_means.test.tests import *

smo_src_path = '../CSC591_ASE_HW_Group12/project_smo/src'
rrp_src_path = '../CSC591_ASE_HW_Group12/project_rrp/src'

print(sys.path)
sys.path.append(smo_src_path)
from project_smo.test.tests import *
print(sys.path)
print(run_smo(4, 16, 'data/auto93.csv'))
sys.path.remove(smo_src_path)

# sys.path.append("../CSC591_ASE_HW_Group12/")
# sys.path.append(rrp_src_path)
# from project_rrp.test.tests import *
# print(sys.path)
# print(run_rrp('data/auto93.csv', 20))
# sys.path.remove(rrp_src_path)
# a = []

# for r in smo:
#   a.append(r.cells)
# print(a)
# sk = ScottKnott({'smo0': a[0], 'smo1': a[1]})
# sk.pprint()   # Prints out the graphs you're used to
# print(sk.get_results())

# print(run_k_means('data/auto93.csv',36,True))