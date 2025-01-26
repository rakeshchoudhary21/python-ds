

# Note:: in below we took profits[i-1] because i is 1 indexed not zero indexed
def rod_cut(profits, i, N):
    if N==0 or i>=len(profits): return 0
    if i > N: return rod_cut(profits,i+1,N)
    else: return max(profits[i-1]+rod_cut(profits,i,N-i), rod_cut(profits,i+1,N))


profits = [1,5,8,9,10,17,17,20]

print(rod_cut(profits,1,8))


profits = [3, 5, 8, 9, 10, 17, 17, 20]
print(rod_cut(profits,1,8))