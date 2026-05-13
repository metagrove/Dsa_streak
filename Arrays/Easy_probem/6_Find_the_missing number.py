arr= [8, 2, 4, 5, 3, 7, 1]

n = len(arr)+1
c = 0

for i in arr:
    c = c+ i
exp = n * (n+1)//2

print(exp-c)