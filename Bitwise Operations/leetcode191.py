'''
Leetcode 191 - Number of 1 bits

Given a positive integer n, write a function that returns the number of set bits in its binary representation 
(also known as the Hamming weight).
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n:
            res += n % 2
            n = n >> 1 
        return res 

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1 
        return res 