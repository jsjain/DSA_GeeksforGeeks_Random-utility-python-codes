import math
def reversebits():
    n = int(raw_input())
    arr = [0]*32

    i = 0
    while n > 0:
        arr[i] = (n %2)
        print n%2
        n /= 2
        i += 1

    size = len(arr)
    for i in range(size/2):
        arr[i],arr[size-i-1] = arr[size-i-1],arr[i]
    print arr

    val = 0
    for i in range(size):
        val += arr[size-i-1]*(int(math.pow(2,size-i-1)))
    print val
reversebits()