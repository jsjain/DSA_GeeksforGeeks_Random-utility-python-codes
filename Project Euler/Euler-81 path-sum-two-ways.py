def minPathSum(mat, n):
    count = 0
    for i in range(n - 1, -1, -1):
        if i is not 0:
            print(min(mat[i][i - 1], mat[i - 1][i]), mat[i - 1][i - 1])
            count += min(mat[i][i - 1], mat[i - 1][i]) + mat[i - 1][i - 1]
    return count + mat[n-1][n-1]


mat = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150],
       [630, 803, 746, 422, 111], [537, 699, 497, 121,
                                   956], [805, 732, 524, 37, 331]]

print(minPathSum(mat, 5))
