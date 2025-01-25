
# Given an expression, we are adding parenthesis to see how many unique results we can get
# ex: 2-1-1 : 2-(1-1) = 2, 2-1-(1)=0, (2)-1-1=0, (2-1-1)=0, unique results =2 that is 2 and 0.

def add_paranthesis(expn):
    # gfg: https://www.geeksforgeeks.org/all-ways-to-add-parenthesis-for-evaluation/
    ans=[]
    for index in range(len(expn)):
        if expn[index] in ('+','-','*','/'):
            op = expn[index]
            L = add_paranthesis(expn[:index])
            R = add_paranthesis(expn[index+1:])

            for l in L:
                for r in R:
                    ans.append(solve(l,r, op))

    if len(ans)==0: ans.append(int(expn))
    return ans

def solve(left,right,operator):
    if operator=='+': return left+right
    if operator=='-': return left-right
    if operator=='/': return left/right
    if operator=='*': return left*right


expn = '2-1-1'
print(add_paranthesis(expn))