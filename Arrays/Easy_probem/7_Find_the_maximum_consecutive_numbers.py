arr = [1, 1, 0, 1, 1, 1]
c =0 
maxi = 0
for i in range(len(arr)):
    if arr[i] ==1:
        c+=1
        maxi = max(maxi,c)
    else:
        c =0 
        
print(maxi)