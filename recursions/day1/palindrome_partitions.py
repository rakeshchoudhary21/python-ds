import sys


# partition a string such that each partition is a palindrome
def is_palindrom(s, i, j):
    str = s[i:j+1]
    reversed = str[::-1]
    return str == reversed


def palindrome_partitions(s,i,j) -> int :
    if i>=j : return 0
    # we can always use the below piece to print the palindrome itself.
    if is_palindrom(s,i,j): return 0
    ans = sys.maxsize
    for k in range(i,j):
        temp = 1+ palindrome_partitions(s,i,k)+ palindrome_partitions(s,k+1,j)
        ans = min(ans,temp)
    return ans

if __name__=='__main__':

    str = "mamdam"
    print(palindrome_partitions(str,0, len(str)))