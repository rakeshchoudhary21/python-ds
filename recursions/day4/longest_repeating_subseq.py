
# its kind of interesting problem.
# take the same string twice, then find lcs but we plus 1 only if i and j are not same index

def longest_repeating_subseq(X,i,j):
    if i>=len(X) or j>=len(X): return 0
    if X[i] ==X[j] and i!=j: return 1+ longest_repeating_subseq(X,i+1,j+1)
    else: return max(longest_repeating_subseq(X,i+1,j), longest_repeating_subseq(X,i,j+1))


X = "AABEBCDD"
print(longest_repeating_subseq(X,0,0))
X= "abcbc"
print(longest_repeating_subseq(X,0,0))