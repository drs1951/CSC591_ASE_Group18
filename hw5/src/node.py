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


class NODE:
    def __init__(self, data, lefts=None, rights=None):
        self.data = data
        self.left = lefts
        self.right = rights

    def walk(self, fun, depth=0):
        """
        Recursively walk the tree, applying a function `fun` to each node.
        
        :param fun: A function to apply to each node. It should accept three arguments:
                    the node, the current depth, and a boolean indicating if it's a leaf.
        :param depth: The current depth in the tree (0 for the root).
        """
        is_leaf = not self.left and not self.right
        fun(self, depth, is_leaf)
        
        if self.left:
            self.left.walk(fun, depth + 1)
        if self.right:
            self.right.walk(fun, depth + 1)

    def show(self, depth=0):
        """
        Display the structure of the tree, printing each node's data.
        """
        def print_node(node, depth, is_leaf):
            indent = "|.. " * depth
            node_info = f"{node.data}" if is_leaf else ""
            print(f"{indent}{node_info}")
        
        self.walk(print_node)