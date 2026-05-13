arr = [4,1,2,1,2]
seen ={}

for i in range(len(arr)):
    num = arr[i]
    if num in seen:
        seen[num] +=1
    else:
        seen[num] = 1
print(seen)

v = min(seen, key= seen.get)
print(v)

        