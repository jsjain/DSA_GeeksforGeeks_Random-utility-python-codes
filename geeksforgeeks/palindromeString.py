def checkPalindrome(half_length, n, s):
    for i in range(half_length):
        if (s[i] != s[n - i - 1]):
            return False
    return True


t = int(input())
while (t > 0):
    n = int(input())
    s = input()

    half_len = n // 2
    if (checkPalindrome(half_len, n, s)):
        print("Yes")
    else:
        print("No")
    t -= 1
