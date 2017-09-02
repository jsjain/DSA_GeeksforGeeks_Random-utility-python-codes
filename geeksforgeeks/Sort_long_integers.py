def comparator(a, b):
    n = len(a)
    m = len(b)
    if(n == m):
        if(long(a) < long(b)):
            return -1
        elif (long(a) > long(b)):
            return 1
        else:
            return 0
    else:
        if(n < m):
            return -1
        elif n > m:
            return 1
        else :
            return 0
        
n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
unsorted.sort(comparator)
for i in unsorted:
    print i
