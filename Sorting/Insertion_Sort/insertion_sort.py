'''
Insertion sort in Python

1. Input an array with values to sort.
2. An outer loop that picks a value to be sorted. For an array with n values, 
this outer loop skips the first value, and must run n-1 times.
3. An inner loop that goes through the sorted part of the array, to find where to insert the value. 
If the value to be sorted is at index i, the sorted part of the array starts at index 0 and ends at index i-1.
'''
def insertionSort(array):

    # Outer Loop
    for step in range(1, len(array)): # Skip first value
        key = array[step]
        j = step - 1                  # n-1 times
        
        # Inner loop
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].      
        # keep shifting elements to the right until we find the correct spot for key.  
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)