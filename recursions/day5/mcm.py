import sys


# classic mcm problem.

def mcm(arr, i, j):
    if i+1>=j: return 0

    ans = sys.maxsize
    for k in range(i+1,j):
        temp = mcm(arr,i,k)+ mcm(arr,k,j)+ arr[i]*arr[k]*arr[j]
        ans = min(ans,temp)

    return ans


matrices = [2,1,3,4]
print(mcm(matrices,0,len(matrices)-1))
matrices = [1, 2, 3, 4, 3]
print(mcm(matrices,0, len(matrices)-1))