arr = [1,2,3,10,4,5]
check = True
for i in range(len(arr)-1):
    if arr[i] >= arr[i+1]:
        check = False
        break
print(check)
        
        
        