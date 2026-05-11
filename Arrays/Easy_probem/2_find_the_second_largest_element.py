def second_largest(arr):
    
    if len(arr)<2:
        return -1
    
    l = float('-inf')
    s = float('-inf')
    for i in range(len(arr)):
        if arr[i] > l:
            s =l
            l = arr[i]
        elif arr[i]> s and arr[i] != l:
            s = arr[i]
    return s

arr =  [1, 2, 4, 7, 7, 5]  
print(second_largest(arr))

"""
arr.sort() 
print(arr)
print(arr[-2])
"""


    
