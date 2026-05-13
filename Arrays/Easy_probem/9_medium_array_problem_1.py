"""
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two """


arr = [1, 0, 2, 1, 0]

c1 = []
c2 = []
c3 = []

for i in range(len(arr)):
    if arr[i] == 0:
        c1.append(arr[i])
        
    elif arr[i] ==1:
        c2.append(arr[i])
    
    else:
        c3.append(arr[i])
print(c1+c2+c3)
