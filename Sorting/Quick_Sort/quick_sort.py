'''
    Quick Sort Algorithm
    
    1. Choose a pivot
    2. Partition the array, elements less than pivot go on left side of pivot and right side vise versa
    3. Recursively apply quick sort to left subarray and right subarray
    4. If the subarray has 0 or 1 element (base case), subarray is sorted   
'''


# This function will be called first to find the pivot's sorted position within the array
# After the pivot's position is found, the quicksort function will be called again to do the sub array tasks.
def partition(arr, low, high):
    
    # Setting pivot as the last element in input array
    pivot = arr[high]
    
    # Initialize pointer i to low - 1 (before the 0th index)
    i = low - 1

    # Iterate through the array from low to high - 1
    for j in range(low, high):
        # If the current element is less than or equal to the pivot
        if arr[j] <= pivot:
            # increment the point and swap the value at arr[i] with arr[j]
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot to the correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    # Returns the index of the pivot 
    return i+1

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Find the pivot's location 1st
        pivot_index = partition(arr, low, high)
        # Once the pivot is found, recursively call quicksort() on the left side of the pivot and right side
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
print("Original Array: ", my_array)
quicksort(my_array)
print("Sorted array:", my_array)
