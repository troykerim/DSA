'''
    Leetcode 278 First Bad Version 
    
    def isBadVersion is an API predifined in the website
'''
def firstBadVersion(n):
    L = 1 
    R = n 
    
    while L < R:
        M = (L + R) // 2 
        if (M):
            R = M 
        else:
            L = M + 1
    return L  


'''
    Brute Force Version
def firstBadVersion(n):
    for x in range(1, n+1):
        if isBadVersion(x):
            return x
'''