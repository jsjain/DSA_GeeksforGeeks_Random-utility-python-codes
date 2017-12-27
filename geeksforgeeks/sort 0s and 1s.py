def sort01(array, size):
    '''
    https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
    '''
    left = 0
    right = size -1
    while left < right:
        while array[left] == 0 and left < right:
            left = left + 1
        while array[right] == 1 and left < right:
            right = right - 1
        if left < right:
            array[left] = 0
            array[right] = 1
            left = left + 1
            right = right - 1
    return array


arr = [0, 1, 0, 1, 1, 1]
arr = sort01(arr, len(arr))
print(arr)

# method 2
'''
count the number of 0s and create a new array with those and
fill rest of the array with 1s
'''

def altsort01(array, size):
    count = 0
    for num in array:
        if num == 0:
            count = count + 1
    new_array = [1] * size
    for i in range(count):
        new_array[i] = 0
    return new_array


arr = [0, 1, 0, 1, 1, 1]
arr = altsort01(arr, len(arr))
print(arr)
