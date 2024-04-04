import random
import math
from project.config import *
from row import *

def any_item(lst):
    return random.choice(lst)

def o(t, ndecs=None):
    if isinstance(t, float):
        return rnd(t, ndecs)
    if isinstance(t, ROW):
        return str(t.cells) + " "
    if not isinstance(t, dict) and not isinstance(t, list):
        return str(t)
    u = []
    for k in t:
        if not str(k).startswith("_"):
            if isinstance(t, list):
                u.append(o(t[k], ndecs))
            else:
                u.append("{}: {}".format(o(k, ndecs), o(t[k], ndecs)))
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

def slice(t, start, stop=None, step=1):
    if start and start < 0:
        start = len(t) + start
    if stop and stop < 0:
        stop = len(t) + stop
    return t[start:stop:step]


def shuffle(t):
    t=t[1:]
    u = t[:]  
    random.shuffle(u)
    return u

def score(t, goal, LIKE, HATE):
    like = hate = 0
    tiny = 1E-30
    # print(t)
    for klass, n in t.items():
        if klass == goal:
            like += n
        else:
            hate += n
    like, hate = like / (LIKE + tiny), hate / (HATE + tiny)
    if hate >= like:
        return 0
    else:
        return like ** the.support / (like + hate)
    
def powerset(s):
    t = [[]]
    for item in s:
        t += [subset + [item] for subset in t]
    return t
