data = input()

def isPalindrome(s):
    return s == s[::-1]

def largestPal():
    maxLen = 0
    larPal = ''
    for i in range(len(data)):
        for j in range(i + 1, len(data) + 1):
            substr = data[i:j]
            if isPalindrome(substr):
                if len(substr) > maxLen:
                    maxLen = len(substr)
                    larPal = substr
    return larPal

print(largestPal())
