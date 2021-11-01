import numpy as np
numbertable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sdktable = [9, 0, 2, 0, 3, 0, 0, 8, 0]


def diff(l1, l2):
    difftable = [i for i in l1 + l2 if i not in l1 or i not in l2]
    return difftable


print(diff(sdktable, numbertable))
