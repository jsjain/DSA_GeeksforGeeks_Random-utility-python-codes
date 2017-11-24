'''
Question: http://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-3/0

logic for question :
for even powers of 2 it gives remainder of 1 else remainer of 2
so just check if binary number is 1 there and if its even then add 1 to remainder
else add 2 to remainder
'''

test = int(input())
while test > 0:
    binary_number = input()
    length = len(binary_number)
    remainder = 0
    for i in range(length):
        if int(binary_number[i]) != 0:
            if i % 2 == 0:
                remainder += 1
            else:
                remainder += 2
    if remainder % 3 == 0:
        print(1)
    else:
        print(0)
    test -= 1
