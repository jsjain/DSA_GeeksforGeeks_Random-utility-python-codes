def randomized_partition(arr, l, r):
    m = 0 if (r - l) == 1 else int((r - l) / 2) + l
    median = sorted([(arr[l], l), (arr[r], r), (arr[m], m)])[1][1]
    pivot = arr[median]
    arr[median], arr[l] = arr[l], arr[median]
    pIndex = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] <= pivot:
            arr[pIndex], arr[j] = arr[j], arr[pIndex]
            pIndex += 1
    arr[l], arr[pIndex - 1] = arr[pIndex - 1], arr[l]
    return pIndex - 1


def randomized_selection(arr, start, end, index):
    if start == end:
        return arr[start]
    pIndex = randomized_partition(arr, start, end)
    k = pIndex - start + 1
    if index == k:
        return arr[pIndex]
    elif index < k:
        return randomized_selection(arr, start, pIndex - 1, index)
    else:
        return randomized_selection(arr, pIndex + 1, end, index - k)


arr = [232, 434, 45345, 4, 5, 64, 43343, 53, 43, 54, 3423, 323, 445, 3, 354]
num = randomized_selection(arr, 0, len(arr) - 1, 8)
arr.sort()
print(arr, arr[7])
print("num at 8th position: {0}".format(num))
