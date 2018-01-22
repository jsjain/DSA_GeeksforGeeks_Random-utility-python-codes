# https://www.geeksforgeeks.org/tiling-problem/

def tiling(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

print(tiling(4))
