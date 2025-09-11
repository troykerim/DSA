'''
    Merge Sort 
    
    Divide & Conquer that sorts an array by first breaking it down into smaller arrays,
    then the building the array back together where the array is sorted.
    
    Divide: Break up the array into smaller and smaller pieces until one such sub-array only consists of 1 element.
    
    Conquer: The algo merges the small pieces of the array back together by putting the lowest value first resulting in a sorted aray.
    
    Breakdown and build up is done recursively.
    
    1. Divide the unsorted array into two sub-arrays, half the size of the original.
    2. Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
    3. Merge two sub-arrays together by always putting the lowest value first.
    4. Keep merging until there are no sub-arrays left.
    
'''
# Divide
def mergeSort(arr):
    # Edge/Base case, if we are giving an empty array or with a 1 element
    if len(arr) <= 1:
        return arr

    # Split array into 2 sub-arrays
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # Divide the left & right sub arrays into more sub arrays
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    # Call the merge function to merge the arrays
    return merge(sortedLeft, sortedRight)

# Conquer
def merge(left, right):
    result = []
    i = j = 0    # pointers to traverse both sub arrays

    '''
    Compare the current element from each half:
    If left[i] is smaller, append it to result and move i forward.
    Otherwise, append right[j] and move j forward.
    Repeat until one of the lists runs out of elements.
    This guarantees the result list stays sorted because each half was already sorted. 
    '''
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
print("Unsorted array: ", unsortedArr)
sortedArr = mergeSort(unsortedArr)
print("\nSorted array:", sortedArr)