
# whether a subset sum is equals to target
def subset_sum(nums,i,target):
    if target==0: return True
    if i>=len(nums): return False
    return subset_sum(nums,i+1, target-nums[i]) or subset_sum(nums,i+1,target)

def subset_with_sum_equal_target(nums,i, target, items):
    if target==0 :
        print(items)
        return

    if i>=len(nums): return

    items.append(nums[i])
    subset_with_sum_equal_target(nums,i+1,target-nums[i],items)
    items.remove(nums[i])
    subset_with_sum_equal_target(nums,i+1,target,items)

# number of subset equal to target, same as above, instead of items itself we give the count
def count_of_subset_sums(nums,i, target):
    if target==0 : return 1

    if i>=len(nums): return 0

    return count_of_subset_sums(nums,i+1,target-nums[i])+count_of_subset_sums(nums,i+1,target)


# there is another problem where we are asked to see if the given array can be divided into 2 halves such that any
# partition is equal to target.


# another q: subset with given difference: [1,2,5] , diff: 2. so we got sub1-sub2 = 2. and sub1+sub2 has to be =8. solving these two we get another target sum problem
# s1-s2=2.
# s1+s2=8
#-----------
# 2s1 = 10, s1 = 5. so we need to find subset whose sum is 5. Note: sum of array is not divisible by 2 then its not a valid difference in question.


# another q: target sum by placing + or -. basically we are dividing the array in 2 halves where one set has all numbers assigned + and other half with -. that is subset with difference problem.

print(subset_sum([2,3,7,61,10], 0,11))
subset_with_sum_equal_target([2,3,7,8,10],0,13,[])
print(count_of_subset_sums([2,3,7,8,10], 0, 18))