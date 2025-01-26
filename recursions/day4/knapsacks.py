

def knapsack_0_1(W,wt, val,i):
    if W==0 or i>= len(wt): return 0
    if wt[i]<=W:
        return max(val[i]+ knapsack_0_1(W-wt[i],wt,val,i+1), knapsack_0_1(W,wt,val,i+1))
    else: return knapsack_0_1(W,wt,val,i+1)



wt = [10, 20, 30]
vals = [60, 100, 120]
W = 50

print(knapsack_0_1(W,wt,vals,0))
