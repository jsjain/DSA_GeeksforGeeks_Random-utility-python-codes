import random


def merge(left, right, a):
    i = j = k = 0
    lenl = len(left)
    lenr = len(right)
    n = len(a)
    while i < lenl and j < lenr:
        if (left[i] < right[j]):
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < lenl:
        a[k] = left[i]
        i += 1
        k += 1
    while j < lenr:
        a[k] = right[j]
        j += 1
        k += 1


def mergesort(arr):
    n = len(arr)
    if n > 1:
        left = mergesort(arr[:int(n / 2)])
        right = mergesort(arr[int(n / 2):])
        merge(left, right, arr)
        return arr
    else:
        return arr


a = [random.randrange(10, 100) for _ in range(0, 10)]
print("Before: ", a)
a = mergesort(a)
print("After: ", a)
