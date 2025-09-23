'''
Neetcode / Leetcode 714

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn)O(logn) time.

'''
def search(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = l + ((r - l) // 2)
        if nums[m] > target:
            r = m
        elif nums[m] <= target:
            l = m + 1
    return l - 1 if (l and nums[l - 1] == target) else -1