def sort012(array, size):
    '''
    https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
    '''
    low = 0
    mid = 0
    high = size - 1
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low = low + 1
            mid = mid + 1
        elif array[mid] == 1:
            mid = mid + 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high = high - 1
    return array


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr = sort012(arr, len(arr))

print(arr)
