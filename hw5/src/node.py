# from l import *

# class NODE:
#     def __init__(self, data):
#         self.here = data
#         self.lefts = None
#         self.rights = None

#     def walk(self, fun, depth=0):
#         fun(self, depth, not (self.lefts or self.rights))
#         if self.lefts:
#             self.lefts.walk(fun, depth + 1)
#         if self.rights:
#             self.rights.walk(fun, depth + 1)

#     def show(self, max_depth=0):
#         def _show(node, depth, is_leaf):
#             post = ""
#             if is_leaf:
#                 d2h_value = rnd(node.here.mid().d2h(self.here))
#                 post = f"{d2h_value}\t{str(node.here.mid().cells)}"
#             nonlocal max_depth
#             max_depth = max(max_depth, depth)
#             print('|.. ' * depth + post)

#         self.walk(_show)
#         print("")
#         print("    " * max_depth, rnd(self.here.mid().d2h(self.here)), str(self.here.mid().cells))
#         print("    " * max_depth, "_", str(self.here.cols.names))