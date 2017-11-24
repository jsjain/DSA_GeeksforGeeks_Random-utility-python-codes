t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i+1] and arr[i] > arr[i+1]:
            print(arr[i])
            break
    t -= 1
