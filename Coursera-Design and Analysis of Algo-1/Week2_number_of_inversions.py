def sort_and_count(a, n):
    if len(a) > 1:
        half = n / 2
        (b, x) = sort_and_count(a[:half], n / 2)
        (c, y) = sort_and_count(a[half:], (n - half))
        (d, z) = merge_and_countsplit(b, c, len(b) + len(c))
        return (d, x + y + z)
    else:
        return (a, 0)


def merge_and_countsplit(b, c, n):
    leftlen = len(b)
    rightlen = len(c)
    d = [0] * n
    z = k = i = j = 0
    while i < leftlen and j < rightlen:
        if (b[i] < c[j]):
            d[k] = b[i]
            i += 1
        else:
            d[k] = c[j]
            j += 1
            z += leftlen - i
        k += 1
    while i < leftlen:
        d[k] = b[i]
        i += 1
        k += 1
    while j < rightlen:
        d[k] = c[j]
        j += 1
        k += 1

    return d, z


a = list()
f = open("arr.txt", "r")
for l in f:
    a.append(int(l))
(a, num) = sort_and_count(a, len(a))
print(num)
