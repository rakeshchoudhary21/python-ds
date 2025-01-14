
# Given a grammar we need to find the kth Symbol.
# N=1 and k=1 then answer is 0
# for any Nth row, first half of the row is opposite of second half, so we need to find for any row if k is in first or second half

def kth_symbol(N,K) -> int:
    if N==1 and K==1: return 0
    else:
        mid = pow(2,N-1)/2
        if K<= mid: return kth_symbol(N-1,K)
        else: return int(not kth_symbol(N-1, K-mid))


print(kth_symbol(2,1))