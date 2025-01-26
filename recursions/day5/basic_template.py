
def solve(arr,i,j):
    #b-c
    if i+1>=j: pass
    for k in range(i+1,j,1):
        temp = solve(arr,i,k)+solve(arr,k,j) + arr[i]*arr[k]*arr[j]
        #update the final answer

    # return the final answer here... thats it.