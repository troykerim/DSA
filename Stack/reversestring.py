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