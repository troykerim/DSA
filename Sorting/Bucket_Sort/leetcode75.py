def sortColors(nums):
    l, r = 0, len(nums) - 1
    i = 0 
    
    def swap(i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    
    while(i <= r):
        if nums[i] == 0:
            swap(l,i)
            l += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1
    return nums
nums = [0, 1, 2, 2, 2, 1, 0]
print("Unsorted Array: ", nums)

print("\nArray sorted: ", sortColors(nums))