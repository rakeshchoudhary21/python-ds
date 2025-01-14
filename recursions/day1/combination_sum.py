# given a bunch of numbers, we need combinations that sum to a target


def combination_sum(arr, target,index,temp:list):
    if target==0:
        print(temp)
    else:
        for i in range(index,len(arr)):
            temp.append(arr[i])
            # below makes lots of sense, we should continue to explore on i+1
            combination_sum(arr,target-arr[i],i+1, temp)
            temp.remove(arr[i])


arr = [2,5,6,6]
# notice though, this solution works fine as long as there are no duplicates
# for duplicates it gives duplicate answers
combination_sum(arr,13,0,[])