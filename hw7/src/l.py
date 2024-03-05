import random
import math

def any_item(lst):
    return random.choice(lst)

def o(t, ndecs=None):
    if isinstance(t, float):
        return rnd(t, ndecs)
    if not isinstance(t, dict):
        return str(t.cells)
    u = []
    for k in t:
        if not str(k).startswith("_"):
            if isinstance(t, list):
                u.append(o(t[k], ndecs))
            else:
                u.append("{}: {}".format(o(k, ndecs), o(t[k], ndecs)))
    print(u)
    return "{" + ", ".join(u) + "}"

def rnd(n, ndecs=2):
    if not isinstance(n, float):
        return n
    if n.is_integer():
        return int(n)
    mult = 10 ** ndecs
    return math.floor(n * mult + 0.5) / mult