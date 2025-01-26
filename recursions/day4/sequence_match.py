
# find if a is a subsequence of b

def match(a,b,i,j,counter):
    if i>=len(a): return counter==len(a)
    if j>=len(b): return False
    if a[i]==b[j]: return match(a,b,i+1,j+1,counter+1)
    else: return match(a,b,i+1,j,counter) or match(a,b,i,j+1,counter)

a = "AXY"
b = "ADXCYY"

print(match(a,b,0,0,0))