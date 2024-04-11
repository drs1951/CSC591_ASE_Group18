from l import *

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
            self.lefts.walk(fun, depth + 1)
        else:
            fun(self, depth, not (self.lefts or self.rights))
        # if self.rights:
        #     self.rights.walk(fun, depth + 1)

    def show(self, stop, max_depth=0):

        def d2h_info(data):
            summ = 0
            maxi = 0
            mini = 1
            n = 0
            data.rows = data.rows[1:]
            data.rows.sort(key=lambda x: x.d2h(data))
            data.rows = data.rows[:stop]
            for row in data.rows:
                n+=1
                dis = row.d2h(data)
                summ += dis
                maxi = max(maxi, dis)
                mini = min(mini, dis)

            print(n)
            print("n")
            
            return {'mean': summ/n, 'min': mini, 'max': maxi}

        def _show(node, depth, is_leaf):
            post = ""
            if is_leaf:
                # d2h_value = rnd(node.here.mid().d2h(self.here))
                post = f"\t{str(node.here.mid().cells)} 890"
                print(d2h_info(node.here))
                print("D@H")
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            print('|.. ' * depth + post)

        self.walk(_show)
        print("")
        print("    " * max_depth, str(self.here.mid().cells))
        print("    " * max_depth, "_", str(self.here.cols.names))