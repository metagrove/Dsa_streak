arr = [2,1,34,0,12,0,122,0,1,0,0,0,2,12]

#========== approch -1 =============

# zeros = []
# nums = []

# for i in range(len(arr)):
#     if arr[i] == 0:
#         zeros.append(arr[i])
#     else:
#         nums.append(arr[i])
# print(nums+zeros)

#========== approch -2 =============

def zeros_to_end(arr):
    j =-1
    
    for i in range(len(arr)):
        if arr[i] == 0:
            j =i
            break
    if j ==-1:
        return -1
    for i in range(j+1,len(arr)):
        if arr[i] !=0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    print(arr)
    
nums = [2,1,34,0,12,0,122,0,1,0,0,0,2,12]
zeros_to_end(nums)



