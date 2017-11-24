t = int(input())
while t > 0:
    n, k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i])
    t -= 1
