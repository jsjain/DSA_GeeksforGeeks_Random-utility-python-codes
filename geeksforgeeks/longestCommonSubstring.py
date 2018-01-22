'''
http://www.geeksforgeeks.org/longest-common-subsequence/
'''

# using memonization method
def longestCommonSubstring(strA, strB, n, m, arrMatrix):
    if arrMatrix[n][m] != None:
        return arrMatrix[n][m]
    if n == 0 or m == 0:
        result = 0
    elif strA[n - 1] == strB[m - 1]:
        result = 1 + longestCommonSubstring(strA, strB, n - 1, m - 1,
                                            arrMatrix)
    else:
        temp1 = longestCommonSubstring(strA, strB, n - 1, m, arrMatrix)
        temp2 = longestCommonSubstring(strA, strB, n, m - 1, arrMatrix)
        result = max(temp1, temp2)
    arrMatrix[n][m] = result
    return result

# using bottoms-up solution
def lcs(strA, strB, n, m):
    arr = [[None for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif strA[i-1] == strB[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
    return arr[n][m]


stringA = 'qwertasdfgy'
stringB = 'qwertydfgdsgdsfgdsfg'
arr = [[None for j in range(len(stringB) + 1)]
       for i in range(len(stringA) + 1)]

finalresult1 = longestCommonSubstring(stringA, stringB, len(stringA),
                                      len(stringB), arr)
print(finalresult1)

finalresult2 = lcs(stringA, stringB, len(stringA), len(stringB))
print(finalresult2)
