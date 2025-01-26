# longest common subsequence

def lcs(a,b,i,j):
    if i>=len(a) or j>=len(b): return 0

    if a[i] == b[j]: return 1+lcs(a,b,i+1,j+1)
    else: return max(lcs(a,b,i+1,j), lcs(a,b,i,j+1))


# longest common substring
def longest_common_substring(a,b,i,j):
    if i>=len(a) or j>=len(b): return 0
    if a[i]==b[j]: return 1+longest_common_substring(a,b,i+1,j+1)
    elif a[i]!=b[j]: return 0
    else: return max(longest_common_substring(a,b,i+1,j), longest_common_substring(a,b,i,j+1))

# shortest common super sequence, shortest super string that contains both given strings in strict order of occurrence
# str1+str2 - lcs(str1,str2) :: this is the answer.
#below finds the actual super string:
def scs(str1,str2,M,N):
    if M>=len(str1): return str2[N:]
    if N>=len(str2): return str1[M:]

    if str1[M] == str2[N]: return str1[M]+ scs(str1,str2,M+1,N+1)

    s1 = scs(str1,str2,M+1,N)
    s2 = scs(str1,str2,M,N+1)
    if len(s1)>len(s2): return str2[N]+s2
    else: return str1[M]+s1


a = "ABCDGH"
b = "ABCDFHG"
print(lcs(a,b,0,0))

print(longest_common_substring(a,b,0,0))
print(scs("geek","eke",0,0))