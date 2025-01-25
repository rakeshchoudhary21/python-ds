
# description: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
# basically nth string is : string at n-1 + "1" + reverse of string at n-1
# Note: for n==1 the string is always 0

def kth_bit_n_binary(n,k):
    if n==1: return 0

    MID = pow(2,n-1)
    if k==MID: return 1
    if k<MID: return kth_bit_n_binary(n-1,k)
    else: return not kth_bit_n_binary(n-1, 2*MID-k)



