'''
Question: http://practice.geeksforgeeks.org/problems/sum-of-numbers-or-number/
'''

t = int(input())

while t > 0:
  x, y = map(int, input().split(" "))
  sum = x + y

  if(len(str(sum)) == len(str(x))):
    print(sum)
  else:
    print(x)
  t -= 1