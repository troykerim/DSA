def minSubArrayLen(target, nums):
    min_length = float('inf')
    start = 0
    total = 0
    
    for end in range(len(nums)):
        total += nums[end]
        
        while total >= target:
            min_length = min(min_length, end - start + 1)
            total -= nums[start]
            start += 1
    
    return 0 if min_length == float('inf') else min_length
print(minSubArrayLen(7, [2,3,1,2,4,3]))  
print(minSubArrayLen(15, [1,2,3,4,5]))   
print(minSubArrayLen(100, [1,2,3]))       