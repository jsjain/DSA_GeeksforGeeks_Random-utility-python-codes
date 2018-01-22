# https://www.geeksforgeeks.org/count-number-ways-tile-floor-size-n-x-m-using-1-x-m-size-tiles/


def countTilingWays(n, m):
    ways = [0] * (n + 1)

    for i in range(1, n + 1):
        if i > m:
            ways[i] = ways[i - 1] + ways[i - m]
        elif i < m:
            ways[i] = 1
        else:
            ways[i] = 2
    return ways[n]


print(countTilingWays(7, 4))
