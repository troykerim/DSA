'''
Leetcode #26 - Remove Duplicates from Sorted Array

You are given an integer array nums sorted in non-decreasing order. 
Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

Note:

    The order of the unique elements should remain the same as in the original array.
    It is not necessary to consider elements beyond the first k positions of the array.
    To be accepted, the first k elements of nums must contain all the unique elements.

Return k as the final result.

Used Two Pointer for this problem
'''
def remove_duplicates(nums):
    # Using Two Pointer (Fast/Slow version)
    if not nums:
        return 0 
    k = 1 
    
    # Implements the "in-place" operation
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1 
            
    return k

nums = [1, 1, 2, 3, 4]

print("Original list: ", nums)
print("Number of non duplicate elements:", remove_duplicates(nums))