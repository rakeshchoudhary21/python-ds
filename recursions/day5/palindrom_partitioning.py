import sys

from recursions.day1.palindrome_partitions import is_palindrom


#classic palindrome partition mcm problem

def partition(s,i,j):
    if i>=j or is_palindrom(s,i,j): return 0

    ans = sys.maxsize

    for k in range(i,j):
        temp = 1+partition(s,i,k)+partition(s,k+1,j)
        ans = min(ans,temp)

    return ans

input = "geek"
print(partition(input,0,len(input)-1))

input = "ababbbabbababa"
print(partition(input,0,len(input)-1))

input = "aaaa"
print(partition(input,0,len(input)-1))