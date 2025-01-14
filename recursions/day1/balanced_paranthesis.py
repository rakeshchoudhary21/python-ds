
# given a number n, generate all parenthesis such that each combination is valid

def balanced_paranthesis( opens:int, closed:int, out:str):
    if opens == 0 and closed ==0 : print(out)
    else:
        if opens!=0: balanced_paranthesis(opens-1, closed, out+"(")
        if closed>opens: balanced_paranthesis(opens,closed-1,out+")")

# its an interesting pattern, pay attention

balanced_paranthesis(2,2,"")

# N bit binary number having more 1s than zeros., similar pattern problem

def n_bit_binary(N, zeros, ones, out):
    if N==0: print(out)
    else:
        n_bit_binary(N-1, zeros,ones+1, out+"1")
        if ones>zeros: n_bit_binary(N-1, zeros+1, ones, out+"0")

n_bit_binary(4,0,0,"")