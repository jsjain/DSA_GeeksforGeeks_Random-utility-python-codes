# https://www.geeksforgeeks.org/stock-buy-sell/


def stockPrice(arr):
    if len(arr) == 1:
        return

    profit = []

    i = 0
    n = len(arr)
    while i< n-1:
        while i < n - 1 and arr[i + 1] <= arr[i]:
            i += 1
        if i == n - 1:
            break
        start = i
        i += 1
        while i < n and arr[i] > arr[i - 1]:
            i += 1
        end = i - 1

        profit.append([start, end])

    if len(profit) == 0:
        print('There is no day when buying the stock will make profitn')
    else:
        totalProfit = 0
        for i in profit:
            totalProfit += arr[i[1]] - arr[i[0]]

        print(totalProfit)


price = [100, 180, 260, 310, 40, 535, 695]
stockPrice(price)
