def binary_search(arr, low, high, v):
    mid = (high - low)/2 + low
    if low > high:
        return -1
    if(arr[mid] == v):
        return mid
    elif (v < arr[mid]):
        high = mid-1
        return binary_search(arr, low, high, v)
    else:
        low = mid + 1
        return binary_search(arr, low, high, v)

v = int(raw_input())
n = int(raw_input())
arr = map(int, raw_input().split(" "))

index = binary_search(arr, 0, n-1, v)
print(index)
