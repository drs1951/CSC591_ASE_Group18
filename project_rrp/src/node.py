from project_rrp.src.l import *

class NODE:
    def __init__(self, data, lefts=None, rights=None):
        self.here = data
        self.lefts = lefts
        self.rights = rights
        self.left = lefts
        self.right = rights


    def walk(self, fun, depth=0):
        # fun(self, depth, not (self.lefts or self.rights))
        if self.lefts:
            return self.lefts.walk(fun, depth + 1)
        else:
            return fun(self, depth, not (self.lefts or self.rights))
        # if self.rights:
        #     self.rights.walk(fun, depth + 1)

    def show(self, stop, data_i, max_depth=0):

        def d2h_info(data):
            summ = 0
            maxi = 0
            mini = 1
            n = 0
            # data.rows = data.rows[1:] ek change
            data.rows.sort(key=lambda x: x.d2h(data_i))
            # print("D2h")
            # print(data.rows[0].d2h(data))
            data.rows = data.rows[:stop]
            # for row in data.rows:
            #     n+=1
            #     dis = row.d2h(data)
            #     summ += dis
            #     maxi = max(maxi, dis)
            #     mini = min(mini, dis)
            #     if dis==0:
            #         print(row.cells)

            # print(n)
            # print("n")
            # print({'mean': summ/n, 'min': mini, 'max': maxi})
            return data.rows[0].d2h(data_i)

        def _show(node, depth, is_leaf):
            post = ""
            if is_leaf:
                # d2h_value = rnd(node.here.mid().d2h(self.here))
                post = f"\t{str(node.here.mid().cells)}"
                # print(d2h_info(node.here))
                # print("D@H")
                return d2h_info(node.here)
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            # print('|.. ' * depth + post)

        # print("")
        # print("    " * max_depth, str(self.here.mid().cells))
        # print("    " * max_depth, "_", str(self.here.cols.names))
        return self.walk(_show)
