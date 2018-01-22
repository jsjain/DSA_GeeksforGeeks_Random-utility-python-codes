# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    if k > 0 and k <= (r-l+1):
        pos = partition(arr, l, r)
        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k - 1:
            return kthSmallest(arr, l, pos - 1, k)

        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
    return None


array = [12, 3, 5, 7, 4, 19, 26]
# 3rd smallest number
k = 3
print(kthSmallest(array, 0, len(array)-1, k))
