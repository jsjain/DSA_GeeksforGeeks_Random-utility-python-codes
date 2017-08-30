t = int(raw_input())
while t > 0:
    n,k = raw_input().split()
    n = int(n)
    k = int(k)
    arr = map(int, raw_input().split())
    arr.sort(reverse= True)
    for i in range(k):
        print (arr[i])
    t -= 1
