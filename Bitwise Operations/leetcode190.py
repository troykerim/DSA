'''
leetcode 190 - Reverse Bits

Reverse bits of a given 32 bits signed integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for i in range(32):
            bit = (n >> i) & 1 
            res = res | (bit << (31 - i))
        return res 