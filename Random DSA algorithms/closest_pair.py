import math


class Point(object):
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y

def distance(point1, point2):
    return math.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)


def merge(left, right, a):
    i = j = k = 0
    lenl = len(left)
    lenr = len(right)
    n = len(a)
    while i < lenl and j < lenr:
        if left[i] < right[j]:
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
        left = mergesort(arr[:n/2])
        right = mergesort(arr[n/2:])
        merge(left, right, arr)
        return arr
    else:
        return arr
