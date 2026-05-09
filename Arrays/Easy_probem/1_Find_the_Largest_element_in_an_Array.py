arr =[2, 5, 1, 3, 0]

"""
arr.sort()
print("The largest number is : ",arr[-1])

"""
"""
largest = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]>largest:
            largest = arr[j]
            
print(largest)

"""
"""
large = arr[0]

for i in range(len(arr)):
    if arr[i] > large:
        large = arr[i]
    
print(large)
"""