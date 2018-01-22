# https://www.geeksforgeeks.org/maximum-product-subarray/

def maximum_product_subarray(arr):
    max_ending_here = 1
    max_so_far = 1
    min_ending_here = 1

    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            max_ending_here *= arr[i]
            min_ending_here = min(min_ending_here*arr[i], 1)

        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1

        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here*arr[i], 1)
            min_ending_here = temp*arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


arr = [-2, -3, 0, -2, -40]

print(maximum_product_subarray(arr))
