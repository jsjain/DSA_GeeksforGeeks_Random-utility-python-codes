import math


def solve(A, B, C):
    tree = [None] * (2**(len(A) + 1) - 1)
    traversingLength = (2**(len(A)+1)) - 2
    tree[0] = B
    for i in range(1, traversingLength, 2):
        parentIndex = int(math.ceil(i / 2) - 1)
        if (tree[parentIndex]):
            prev = 'heaven'
            if tree[parentIndex] < C:
                prev = 'hell'
            aindex = math.floor(math.log(i, 2)) - 1
            if (tree[parentIndex]):
                left = max((tree[parentIndex] - A[aindex]), 0)
                currLeft = 'hell'
                if (left >= C):
                    currLeft = 'heaven'
                if (prev == 'heaven'):
                    tree[i] = left
                if (prev == 'hell' and currLeft == 'heaven'):
                    tree[i] = left

                right = min((tree[parentIndex] + A[aindex]), 2 * C)
                currRight = 'hell'
                if (right >= C):
                    currRight = 'heaven'
                if (prev == 'heaven'):
                    tree[i + 1] = right
                if (prev == 'hell' and currRight == 'heaven'):
                    tree[i + 1] = right
    # counting
    count = 0
    for i in range(1, len(tree)):
        if (tree[i]):
            parentIndex = int(math.ceil(i / 2) - 1)
            if (tree[i] < C) and tree[parentIndex] >= C:
                count = count + 1
            if tree[parentIndex] < C and tree[i] >= C:
                count = count + 1
    return count


A = [6, 9, 2, 2, 2]
B = 12
C = 10
print(solve(A, B, C))
