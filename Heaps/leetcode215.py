'''
leetcode 215 - Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l 
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], num[r] = nums[r], nums[p]
            
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p+1, r)
            else: return nums[p]
        return quickSelect(0, lens(nums)-1)