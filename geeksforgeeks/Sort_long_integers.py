def comparator(a, b):
    n = len(a)
    m = len(b)
    if n == m:
        if int(a) < int(b):
            return -1
        elif int(a) > int(b):
            return 1
        else:
            return 0
    else:
        if n < m:
            return -1
        elif n > m:
            return 1
        else:
            return 0


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
unsorted.sort(comparator)
for i in unsorted:
    print(i)
