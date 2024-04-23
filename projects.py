import sys
import os

from raise_utils.interpret import ScottKnott
from project_k_means.test.tests import *
from project_smo.test.tests import *
from project_rrp.test.tests import *

smo_src_path = '../CSC591_ASE_HW_Group12/project_smo/src'
rrp_src_path = '../CSC591_ASE_HW_Group12/project_rrp/src'
kms_src_path = '../CSC591_ASE_HW_Group12/project_k_means/src'

sys.path.append(smo_src_path)

# smo9 = run_smo(4, 5, 'data/auto93.csv')
# # smo20 = run_smo(4, 16, 'data/auto93.csv')
# # smo32 = run_smo(4, 28, 'data/auto93.csv')
# # smo64 = run_smo(4, 60, 'data/auto93.csv')
# sys.path.remove(smo_src_path)

# sys.path.append("../CSC591_ASE_HW_Group12/")
# sys.path.append(rrp_src_path)
# sys.path.append(kms_src_path)
# print(run_k_means('data/auto93.csv', 32, False)[1])
# print(run_smo(4, 28, 'data/auto93.csv')[1])
# print(run_rrp('data/auto93.csv', 32)[1])

# rrp9 = run_rrp('data/auto93.csv', 9)
# # rrp20 = run_rrp('data/auto93.csv', 20)
# # rrp32 = run_rrp('data/auto93.csv', 32)
# # rrp64 = run_rrp('data/auto93.csv', 64)
# sys.path.remove(rrp_src_path)


# sys.path.append("../CSC591_ASE_HW_Group12/project_k_means/src")
# print(run_k_means('data/auto93.csv', 36, False))
# print(run_k_means('data/auto93.csv', 36, True))

times = {}

for folder_name in os.listdir('data'):
    folder_path = os.path.join('data', folder_name)
    
    if os.path.isdir(folder_path):
        # Loop through each CSV file in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith("final.csv"):
                file_path = os.path.join(folder_path, file_name)
                # print(file_path)
                smo9 = run_smo(4, 5, file_path)
                smo20 = run_smo(4, 16, file_path)
                smo32 = run_smo(4, 28, file_path)
                smo64 = run_smo(4, 60, file_path)
                rrp9 = run_rrp(file_path, 9)
                rrp20 = run_rrp(file_path, 20)
                rrp32 = run_rrp(file_path, 32)
                rrp64 = run_rrp(file_path, 64)
                kmeans9 = run_k_means(file_path, 9, False)
                kmeans20 = run_k_means(file_path, 20, False)
                kmeans32 = run_k_means(file_path, 32, False)
                kmeans64 = run_k_means(file_path, 64, False)
                kmeanspp9 = run_k_means(file_path, 9, True)
                kmeanspp20 = run_k_means(file_path, 20, True)
                kmeanspp32 = run_k_means(file_path, 32, True)
                kmeanspp64 = run_k_means(file_path, 64, True)
                rand9 = run_rand(file_path, 9)
                rand20 = run_rand(file_path, 20)
                rand32 = run_rand(file_path, 32)
                rand64 = run_rand(file_path, 64)
                print(file_name)
                print()
                sk = ScottKnott({
                  'smo9': smo9[0],
                  'smo20': smo20[0],
                  'smo32': smo32[0],
                  'smo64': smo64[0],
                  'rrp9': rrp9[0],
                  'rrp20': rrp20[0],
                  'rrp32': rrp32[0],
                  'rrp64': rrp64[0],
                  'kmeans9': kmeans9[0],
                  'kmeans20': kmeans20[0],
                  'kmeans32': kmeans32[0],
                  'kmeans64': kmeans64[0],
                  'kmeanspp9': kmeanspp9[0],
                  'kmeanspp20': kmeanspp20[0],
                  'kmeanspp32': kmeanspp32[0],
                  'kmeanspp64': kmeanspp64[0],
                  'rand9': rand9,
                  'rand20': rand20,
                  'rand32': rand32,
                  'rand64': rand64
                })
                sk.pprint()   
                print("__________________________________________________________________________________________")
                print()

                # cur_time = {
                #   'smo9': smo9[1],
                #   'smo20': smo20[1],
                #   'smo32': smo32[1],
                #   'smo64': smo64[1],
                #   'rrp9': rrp9[1],
                #   'rrp20': rrp20[1],
                #   'rrp32': rrp32[1],
                #   'rrp64': rrp64[1],
                #   'kmeans9': kmeans9[1],
                #   'kmeans20': kmeans20[1],
                #   'kmeans32': kmeans32[1],
                #   'kmeans64': kmeans64[1],
                #   'kmeanspp9': kmeanspp9[1],
                #   'kmeanspp20': kmeanspp20[1],
                #   'kmeanspp32': kmeanspp32[1],
                #   'kmeanspp64': kmeanspp64[1]
                # }
                # times[file_name] = cur_time

# print("____________________________________________________________")
# print()
# print(times)
# print("____________________________________________________________")
# print("Printed above part for safety")
# print("____________________________________________________________")


# print()
# print("____________________________________________________________")
# print("File Name    SMO9   SMO20   SMO32   SMO64   RRP9   RRP20   RRP32   RRP64   KMeans9   KMeans20   KMeans32   KMeans64   KMeansPP9   KMeansPP20   KMeansPP32   KMeansPP64")
# print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# for file_name, cur_time in times.items():
#     print(f"{file_name:<13}", end="")
#     for key in ['smo9', 'smo20', 'smo32', 'smo64', 'rrp9', 'rrp20', 'rrp32', 'rrp64', 'kmeans9', 'kmeans20', 'kmeans32', 'kmeans64', 'kmeanspp9', 'kmeanspp20', 'kmeanspp32', 'kmeanspp64']:
#         print(f"{cur_time.get(key, ''):<8}", end="")
#     print()



# # for r in smo:
# #   a.append(r.cells)
# # print(a)
# sk = ScottKnott({'smo9': smo9, 'smo20': smo20, 'smo32': smo32, 'smo64': smo64, 'rrp': rrp})
# sk.pprint()   # Prints out the graphs you're used to
# print(min(smo))
# print(min(rrp))
# # print(sk.get_results())
