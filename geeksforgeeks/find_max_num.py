t = int(raw_input())
while t > 0:
    n = int(input())
    arr = map(int, raw_input().split())
    for i in range(n):
        if(arr[i+1] and arr[i] > arr[i+1]):
            print arr[i]
            break
    t -= 1
