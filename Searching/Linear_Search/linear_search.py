def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 


arr = [3, 7, 9, 2, 6, 5]
target = 9 

result = linear_search(arr, target)

if result != -1:
    print(f"The value {target} was found at index: {result}")
else:
    print(f"The value {target} was not found.")