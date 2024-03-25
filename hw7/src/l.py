import random
import math
from hw7.config import *

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

def score(t, goal, LIKE, HATE):
    like = hate = 0
    tiny = 1E-30
    for klass, n in t.items():
        if klass == goal:
            like += n
        else:
            hate += n
    like = like / (LIKE + tiny)
    hate = hate / (HATE + tiny)
    if hate > like:
        return 0
    else:
        return like ** the.support / (like + hate)
    
def entropy(t):
    n = sum(t.values())  # Total count of items
    e = 0  # Entropy
    for v in t.values():
        p = v / n  # Probability of each item
        e = e - p * math.log(p, 2)  # Accumulate entropy
    return e, n