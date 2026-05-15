"""
Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
Output : YES
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].

Input: N = 5, arr[] = {2,6,5,8,11}, target = 15
Output : NO.
Explanation: There exist no such two numbers whose sum is equal to the target. 
"""
# ========================= approch-1 =========================
arr = [2,6,5,8,11]

target = 14

# for i in range(len(arr)):
#     for j in range(1,len(arr)):
#         if arr[i]+arr[j] == target:
#             print(i,j)
#             break

# ========================= approch-2 =========================
