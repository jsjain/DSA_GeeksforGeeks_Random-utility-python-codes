def insertionSort(arr, m):
    to_insert = arr[m - 1]
    j = m - 2
    while (to_insert < arr[j] and j >= 0):
        arr[j + 1] = arr[j]
        for i in arr:
            print(i),
        print("")
        j -= 1
    arr[j + 1] = to_insert
    for i in arr:
        print i,


m = int(raw_input())
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar, m)
