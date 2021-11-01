import numpy as np
sdkTable = np.zeros((9, 9), dtype=int)
numberTable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
solving = True
rowMissing = []
columnMissing = []
squareMissing = []
sdkTable[0, 0] = 1
sdkTable[1, 0] = 2
sdkTable[2, 0] = 3
sdkTable[0, 8] = 4


def diff(l1, l2):
    difftable = [i for i in l1 + l2 if i not in l1 or i not in l2]
    return difftable


"""
example table:
       c c c   c c c   c c c
       1 2 3   4 5 6   7 8 9
row 1 [0 0 0 | 0 0 0 | 0 0 0]
row 2 [0 0 0 | 0 0 0 | 0 0 0]
row 3 [0 0 0 | 0 0 0 | 0 0 0]
      -----------------------
row 4 [0 0 0 | 0 0 0 | 0 0 0]
row 5 [0 0 0 | 0 0 0 | 0 0 0]
row 6 [0 0 0 | 0 0 0 | 0 0 0]
      -----------------------
row 7 [0 0 0 | 0 0 0 | 0 0 0]
row 8 [0 0 0 | 0 0 0 | 0 0 0]
row 9 [0 0 0 | 0 0 0 | 0 0 0]
"""
print(sdkTable)
# while solving:
    # Analyze phase
    # Analyze rows:
for row in range(0, 9):
    rowMissing.append(diff(list(sdkTable[row, 0:9]), numberTable))
for column in range(0, 9):
    columnMissing.append(diff(list(sdkTable[0:9, column]), numberTable))
for squareX in range(0, 3):
    for squareY in range(0, 3):
        sSX1 = squareX * 3
        sSX2 = squareX * 3 + 3
        sSY1 = squareY * 3
        sSY2 = squareY * 3 + 3
        squareList = sdkTable[sSX1:sSX2, sSY1:sSY2]
        squareMissing.append(diff(list(squareList.flatten()), numberTable))

print(rowMissing)
print(columnMissing)
print(squareMissing)
