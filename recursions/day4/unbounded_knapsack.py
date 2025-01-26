
# in unbounded knapsack we can include same item multiple times.

def unbounded_knapsack(W,wt, val,i):
    if W==0 or i>= len(wt): return 0
    if wt[i]>W: return unbounded_knapsack(W,wt,val,i+1)
    else: return max(val[i]+unbounded_knapsack(W-wt[i],wt,val,i), unbounded_knapsack(W,wt,val,i+1))


capacity = 8
val = [10,40,50,70]
wt = [1,3,4,5]

print(unbounded_knapsack(capacity, wt, val,0))


val = [5,4,3,21]
wt = [1,2,3,4]
capacity = 8
print(unbounded_knapsack(capacity, wt, val,0))

Output: 48