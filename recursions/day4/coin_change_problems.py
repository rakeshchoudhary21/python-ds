import sys


# these are various coin change problems

# number of ways to get a change

def coin_change_ways(coins, target,i):
    if target==0: return 1
    if i>=len(coins): return 0

    if coins[i]>target: return coin_change_ways(coins,target,i+1)
    else: return coin_change_ways(coins,target-coins[i],i) + coin_change_ways(coins,target,i+1)


# min coins to form a change


def coin_change_min(coins, target,i):
    if target==0: return 0
    if i>=len(coins): return sys.maxsize

    if coins[i]>target: return coin_change_min(coins,target,i+1)
    else: return min(1+coin_change_min(coins,target-coins[i],i+1), coin_change_min(coins,target,i+1))



coins = [1,2,3]
change = 5
# 1+1+1+1+1, 1+1+3, 1+1+1+2, 2+3, 1+2+2
print(coin_change_ways(coins,change,0))

coins = [200]
change = 100
print(coin_change_ways(coins,change,0))

coins = [1,2,3,4]
change = 6
print(coin_change_min(coins,change,0))