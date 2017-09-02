t = int(input())
while t > 0:
    n= int(input())
    arr = list(map(int, raw_input().split()))
    pos_arr = []
    neg_arr = []
    for i in range(n):
        if(arr[i] >= 0):
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])
    pos_len = len(pos_arr)
    neg_len = len(neg_arr)
    i = j = 0
    print_string = ''
    while i < pos_len and j < neg_len :
        print_string += str(pos_arr[i]) + " " + str(neg_arr[j]) + " " 
        i += 1
        j += 1
    while i < pos_len:
        print_string += str(pos_arr[i])
        i += 1
    while j < pos_len:
        print_string += str(pos_arr[j])
        j += 1
    print (print_string)
    t -= 1
