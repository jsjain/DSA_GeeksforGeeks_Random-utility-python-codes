'''
https://www.geeksforgeeks.org/maximum-weight-path-ending-element-last-row-matrix/
'''

def maxWeightPath_recusive(mat, i , j, height):
    if i == 0 and j == 0:
        return mat[0][0] + max(
            maxWeightPath_recusive(mat, i + 1, j, height),
            maxWeightPath_recusive(mat, i + 1, j + 1, height))
    if i == height:
        return mat[i][j]
    else:
        return mat[i][j] + max(
            maxWeightPath_recusive(mat, i + 1, j, height),
            maxWeightPath_recusive(mat, i + 1, j + 1, height))


matrix = [[4, 2, 3, 4, 1], [2, 9, 1, 10, 5], [15, 1, 3, 0, 20],
          [16, 92, 41, 44, 1], [8, 142, 6, 4, 8]]

result = maxWeightPath_recusive(matrix, 0, 0, 4)
print(result)

#  using DP


def maxWeightPath(mat, n):
    dp = [[0 for i in range(n)] for j in range(n)]

    dp[0][0] = mat[0][0]

    for i in range(1, n):
        dp[i][0] = mat[i][0] + dp[i-1][0]

    for i in range(1, n):
        j = 1
        while (j < (i + 1)) and (j < n):
            dp[i][j] = mat[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            j = j + 1
    result = 0
    for i in range(n):
        if result < dp[n-1][i]:
            result = dp[n-1][i]
    return result

result = maxWeightPath(matrix, 5)
print(result)
