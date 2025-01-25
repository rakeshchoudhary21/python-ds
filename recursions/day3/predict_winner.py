

# given list of numbers, p1 and p2 pick numbers from left or right most end of array. we need to find if possible for p1 to win

def predict_winner(nums):
    # 0 is p1 turn and 1 is p2 turn
    return solve(nums,0,0, 0,len(nums)-1,0)

def solve(nums,p1_score,p2_score, i,j,turn):
    if i>j: return p1_score>=p2_score

    else:
        if turn==0:
            return solve(nums,p1_score+nums[i],p2_score,i+1,j,1) or solve(nums,p1_score+nums[j],p2_score,i,j-1,1)
        else:
            return not (not solve(nums, p1_score, p2_score+nums[i], i + 1, j, 0) or not solve(nums, p1_score, p2_score+nums[j],
                                                                                   i, j - 1, 0))


nums = [11,-16,5]
print(predict_winner(nums))