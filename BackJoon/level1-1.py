import sys

def palindrome(a, left, right):
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            res1 = palindrome(a, left+1, right)
            res2 = palindrome(a, left, right-1)
            if res1 == True or res2 == True:
                return True
            else:
                return False
    return True


a = list(sys.stdin.readline()) #입력값
result = palindrome(a, 0, len(a)-1)
print(result)