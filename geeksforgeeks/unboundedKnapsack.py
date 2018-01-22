# https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/


def unboundedKnapsack(W, val, wt):
    dp = [0]*(W+1)

    for i in range(W+1):
        for j in range(len(val)):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i-wt[j]] + val[j])
    return dp[W]

W = 100
val = [10, 30, 20]
wt = [5, 10, 15]

print(unboundedKnapsack(W, val, wt))
