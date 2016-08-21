A= [ 1, 2, 5, -7, 2, 5 ]
def smallestsubarr(A):
    n = len(A)
    i = 0
    maxsum = 0
    arr = []
    finalarr = []
    su = 0
    while i < n:
        while (A[i] >= 0) and (i < n-1) :
            # print i
            su += A[i]
            arr.append(A[i])
            i += 1

        if su > maxsum:
            maxsum = su
            su = 0
            finalarr = []
            finalarr = arr
            arr = []
        i += 1
    print finalarr
smallestsubarr(A)