# https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number/
# https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/
import functools

func = lambda x, y: -1 if str(x) + str(y) > str(y) + str(x) else 1

arr = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]

sortedArr = sorted(arr, key=functools.cmp_to_key(func))
print(''.join(str(x) for x in sortedArr))

# naive approach using bubble sort

length = len(arr)
for i in range(length-1):
    for j in range(i+1, length):
        if func(arr[i], arr[j]) == 1:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
