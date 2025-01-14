
# given a target X, we need to tell in how many ways we can achieve X by adding or subtracting given numbers
# basically we are putting + or - in front of each number to get the target

def ways_to_get_target(target, arr, current_sum,i):
    if i>= len(arr):
        if current_sum==target: return 1
        return 0

    return ways_to_get_target(target, arr, current_sum+arr[i],i+1)+ways_to_get_target(target,arr,current_sum-arr[i],i+1)


print(ways_to_get_target(5,[1,1,1,1,1],0,0))

