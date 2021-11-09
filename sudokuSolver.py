import numpy as np
import time
# sdkTable = np.zeros((9, 9), dtype=int)
global sdkTable, solving, rowMissing, columnMissing, squareMissing
# Assign table
sdkTable = np.array([[0, 0, 0, 2, 6, 0, 7, 0, 1],
                    [6, 8, 0, 0, 7, 0, 0, 9, 0],
                    [1, 9, 0, 0, 0, 4, 5, 0, 0],
                    [8, 2, 0, 1, 0, 0, 0, 4, 0],
                    [0, 0, 4, 6, 0, 2, 9, 0, 0],
                    [0, 5, 0, 0, 0, 3, 0, 2, 8],
                    [0, 0, 9, 3, 0, 0, 0, 7, 4],
                    [0, 4, 0, 0, 5, 0, 0, 3, 6],
                    [7, 0, 3, 0, 1, 8, 0, 0, 0]])
NUMBERTABLE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
solving = True
rowMissing = []
columnMissing = []
squareMissing = []


def diff(l1, l2):  # Returns the difference in two different lists
		# If the combined list of l1 and l2 has any values that are not in both,
		# then it will be in diffTable
    diffTable = [i for i in l1 + l2 if i not in l1 or i not in l2]
    return diffTable


def sim(l1, l2, l3):  # Returns the similar values in three different lists
    tempL = []
    for a in range(0, len(l1)):
        for b in range(0, len(l2)):
            for c in range(0, len(l3)):
								# If three values from lists a, b and c are the same:
                if l1[a] == l2[b] == l3[c]:
                    tempL.append(l1[a])
    return tempL


def findOne():  # Will find a tile that only has one missing number
    for x in range(0, 9):
        for y in range(0, 9):
						# The index from squareMissing is gotten from the x value floor divided by three, times three,
						# and the y value is simply floor divided by three and added to x. e.g. x = 8, y = 2
						# x // 3 = 2, times 3 is 6. y // 2 = 0, so it would be the 6th value in the list.
						# square 1 = (0, 0) to (3, 3), square 2 = (3, 3) to (6, 3), etc.
            missing = sim(rowMissing[x], columnMissing[y], squareMissing[(x // 3 * 3) + y//3])
            if len(missing) == 1:
                if sdkTable[x, y] == 0:
                    return x, y, missing[0]


print(f"Input: \n{sdkTable}")
while solving:
    # Analyze phase
    rowMissing = []
    columnMissing = []
    squareMissing = []
    for row in range(0, 9):  # Analyze rows, or the differences
        rowMissing.append(diff(list(sdkTable[row, 0:10]), NUMBERTABLE))
    for column in range(0, 9):  # Analyze columns, or the differences
        columnMissing.append(diff(list(sdkTable[0:10, column]), NUMBERTABLE))
    for squareX in range(0, 3):  # Analyze "squares" (3x3 sections)
        for squareY in range(0, 3):
            sSX1 = squareX * 3
            sSX2 = squareX * 3 + 3  # The three is added because it's the outer edge, 0, 0 and 3, 3
            sSY1 = squareY * 3
            sSY2 = squareY * 3 + 3  # Same as above
            squareList = sdkTable[sSX1:sSX2, sSY1:sSY2]
            squareMissing.append(diff(list(squareList.flatten()), NUMBERTABLE))
		# If a square that only has one solution is empty:
    if sdkTable[findOne()[0], findOne()[1]] == 0: 
				# The square will be filled with the solution
        sdkTable[findOne()[0], findOne()[1]] = findOne()[2]  # sdkTable[x, y] = missing
    try:  # Try-except catch is only to prevent the list from being empty/negative
        rowMissing[findOne()[0]].remove(findOne()[2])
    except TypeError:
        pass
    if 0 not in sdkTable:  # If there are no more empty spaces left:
        solving = False  # Break the loop
print(f"\nResult: \n{sdkTable}")

