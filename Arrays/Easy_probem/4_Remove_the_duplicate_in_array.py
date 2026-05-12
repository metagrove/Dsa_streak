arr = [1, 2, 4,4,4, 6, 7, 5]
""" ==================== approch 1 ==================

seen= []

for i in arr:
    if i not in seen:
        seen.append(i)
        
print(seen)

"""
#======================= approch -2 ===================

i =0

for j in range(1,len(arr)):
    if arr[j] != arr[i]:
        i+=1
        arr[i] = arr[j]
    v = i+1
print(v)
print(arr[:v])