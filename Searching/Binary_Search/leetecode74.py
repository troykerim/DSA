'''
Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''

def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    
    top, bot = 0, rows - 1 
    while top <= bot:
        row = (top + bot) // 2 
        if target > matrix[row][-1]:
            top = row + 1 
        elif target < matrix[row][0]:
            bot = row - 1  
        else:
            break
    
    if not (top <= bot):
        return False
        
    row = (top + bot) // 2 
    l, r = 0, cols - 1 
    while l <= r:
        m = (l + r) // 2 
        if target > matrix[row][m]:
            l = m + 1 
        elif target < matrix[row][m]:
            r = m - 1 
        else:
            return True 
        return False  
    
