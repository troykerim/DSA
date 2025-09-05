'''
    Implementation of Bubble Sort Algorithm
'''

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse over entire array
    for i in range(n):
        swap = False 
        # Last i elements are in place
        for j in range(0, n - i - 1):
            # Swap if element left side is greater than right side [j] vs [j+1]
            # A temp variable could also be used
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True 
        if (swap == False):
            break 
        

arr = [9, 1, 8, 7, 3, 2, 4, 5, 6]

print("Original array: ", arr)
bubbleSort(arr)
print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i], end = ' ')
print()