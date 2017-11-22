from random import randint

def kadane(arr):
  max_current = max_global = arr[0]
  for i in range(1, len(arr)):
    print(max_current, max_global)
    max_current = max(arr[i], max_current + arr[i])
    if max_current > max_global:
      max_global = max_current
  return max_global


arr = [randint(-100, 100) for _ in range(10)]
print("Arr: ", arr)
print("maxSubArrSum = ", kadane(arr))
