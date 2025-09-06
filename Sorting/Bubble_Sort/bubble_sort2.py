'''
Short bubble sort implementation

A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known. 
These “wasted” exchange operations are very costly. 
However, because the bubble sort makes passes through the entire unsorted portion of the list, 
it has the capability to do something most sorting algorithms cannot. 
In particular, if during a pass there are no exchanges, then we know that the list must be sorted. 
A bubble sort can be modified to stop early if it finds that the list has become sorted. 
This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop. 
 '''
def shortBubbleSort(alist):
    exchanges = True
    num = len(alist)-1
    
    while num > 0 and exchanges:
       exchanges = False
       
       for i in range(num):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       num = num-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)