'''
https://www.geeksforgeeks.org/gold-mine-problem/
'''

def goldMiner(gold, n, m):
    goldTable = [[0 for x in range(n)] for y in range(m)]

    for col in range(m-1, -1, -1):
        for row in range(n-1, -1, -1):
            right = 0 if col == n-1 else goldTable[row][col + 1]
            right_up = 0 if ((row == 0) or (col == m-1)) else goldTable[row-1][col+1]
            right_down = 0 if ((row == n-1) or (col == m-1)) else goldTable[row-1][col-1]

            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) 
    result = goldTable[0][0]
    for i in range(n):
        if result < goldTable[i][0]:
            result = goldTable[i][0]
    return result

gold_matrix = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]

result = goldMiner(gold_matrix, 4, 4)
print(result)
