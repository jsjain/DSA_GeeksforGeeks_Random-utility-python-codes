# quick sort algo implementation as per coursera Divide and Conquer Week 3

def quick_sort(arr,start, end):
    if(start < end):
        pivotIndex = partition_last(arr, start, end)
        inversion = end-start
        inversion += quick_sort(arr, start, pivotIndex-1)
        inversion += quick_sort(arr, pivotIndex+1, end)
        return inversion
    else:
        return 0

# when pivot element is first elemnt in the array
def partition_first(arr, l, r):
    pivot = arr[l]
    pIndex = l+1
    for j in range(l+1,r+1):
        if(arr[j] <= pivot):
            arr[pIndex], arr[j] = arr[j], arr[pIndex]
            pIndex += 1
    arr[l], arr[pIndex-1] = arr[pIndex-1], arr[l]
    return pIndex-1

# when pivot element is last element in the array
def partition_last(arr, l, r):
    pivot = arr[r]
    # swapping the last elment with first element and then its just same
    # partitioning with first element therefore the code is also same
    arr[r], arr[l] = arr[l], arr[r]
    pIndex = l+1
    for j in range(l+1,r+1):
        if(arr[j] <= pivot):
            arr[pIndex], arr[j] = arr[j], arr[pIndex]
            pIndex += 1
    arr[l], arr[pIndex-1] = arr[pIndex-1], arr[l]
    return pIndex-1

# when pivot element is chosen from median of
#  first, last and middle element
def partition_median(arr, l, r):
    m = 0 if (r - l) == 1 else int((r - l)/2) + l
    median = sorted([(arr[l],l), (arr[r],r), (arr[m],m)])[1][1]
    pivot = arr[median]
    arr[median], arr[l] = arr[l], arr[median]
    pIndex = l+1
    for j in range(l+1,r+1):
        if(arr[j] <= pivot):
            arr[pIndex], arr[j] = arr[j], arr[pIndex]
            pIndex += 1
    arr[l], arr[pIndex-1] = arr[pIndex-1], arr[l]
    return pIndex-1



# a = [545,5667,2,4245,650,767,43458,35,43646,79,9,4565,65,323,42,4]
# inversion = quick_sort(a, 0, len(a)-1)
# print a
# print inversion


fh = open("quick_sort_file.txt", 'r')
arr = []
for line in fh:
    arr.append(int(line))
inversion = quick_sort(arr, 0, len(arr)-1)
print (inversion)