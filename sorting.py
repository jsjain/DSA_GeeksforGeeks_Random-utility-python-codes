# Implementation of common sorting algorithms

a = [6, 9, 96, 54, 3, 7, 554, 5, 4, 56, 554, 554]


# bubble sort
def bubblesort(a):
    n = len(a)
    i = 0
    while (i < n - 1):
        j = 0
        while (j < n - i - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    print(a)


# Selection sort
def selectionsort(a):
    k = len(a)
    for i in range(0, k):
        minint = a[i]
        for j in range(i, k):
            if (minint > a[j]):
                minint = a[j]
                minintindex = j
        a[i], a[minintindex] = a[minintindex], a[i]

    print(a)


# selectionsort([6,9,54,96,3,7,4,554,56])


# insertion sort
def insertionsort(a):
    k = len(a)

    for i in range(1, k):
        for j in range(0, i):
            if (a[i] < a[j]):
                t = a[i]
                for l in range(i, j, -1):
                    a[l] = a[l - 1]
                a[j] = t
    print(a)


# insertionsort([6,9,96,54,3,7,4,554,56])


# merge sort
def mergesort(a):
    n = len(a)

    if (n > 1):
        mid = n / 2
        left = a[:mid]
        right = a[mid:]

        mergesort(left)
        mergesort(right)
        merge(left, right, a)


def merge(left, right, a):
    nl = len(left)
    nr = len(right)
    i = j = k = 0
    while ((i < nl) and (j < nr)):
        if (left[i] < right[j]):
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while (i < nl):
        a[k] = left[i]
        i += 1
        k += 1
    while (j < nr):
        a[k] = right[j]
        j += 1
        k += 1


# quick sort
def quicksort(a, start, end):
    if (start < end):
        pindex = hpartition(a, start, end)
        quicksort(a, start, pindex)
        quicksort(a, pindex + 1, end)


def partition(a, start, end):
    pivot = a[end]
    pindex = 0
    for i in range(0, end):
        if (a[i] <= pivot):
            a[i], a[pindex] = a[pindex], a[i]
            pindex += 1
    a[pindex], a[end] = a[end], a[pindex]
    return pindex


def hpartition(a, start, end):
    pivot = a[start]
    i = start - 1
    j = end + 1

    while True:
        while True:
            i += 1
            if not (i < j and (a[i] < pivot)):
                break
        while True:
            j -= 1
            if not (j >= i and (a[j] > pivot)):
                break

        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
        print a
        print start, end


quicksort(a, 0, len(a) - 1)
print a