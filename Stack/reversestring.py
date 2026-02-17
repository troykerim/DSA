'''
Leetcode 344 - reverse a string
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Stack solution
        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
            
'''

Two Pointer Solution

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1 
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

'''