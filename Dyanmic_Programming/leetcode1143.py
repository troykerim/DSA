'''
leetcode 1143 - Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        @cache
        def longest(i,j):
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                return 1 + longest(i+1, j+1)
            else:
                return max(longest(i, j+1), longest(i+1, j))
        return longest(0, 0)