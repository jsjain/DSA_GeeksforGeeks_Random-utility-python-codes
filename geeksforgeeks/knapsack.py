# https://www.geeksforgeeks.org/knapsack-problem/


def knapsack_recursive(value, weight, leftWeight, n):
    if n == 0 or leftWeight == 0:
        return 0
    if weight[n - 1] > leftWeight:
        return knapsack_recursive(value, weight, leftWeight, n - 1)
    else:
        return max((value[n - 1] +
                    knapsack_recursive(value, weight,
                                       (leftWeight - weight[n - 1]), n - 1)),
                   knapsack_recursive(value, weight, leftWeight, n - 1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
result = knapsack_recursive(val, wt, W, n)
print(result)


#  Using DP
def knapsack(W, wt, val, n):
    k = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i - 1] <= w:
                k[i][w] = max((val[i-1] + k[i-1][w - wt[i - 1]]), k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    return k[n][W]


result = knapsack(W, wt, val, n)
print(result)
