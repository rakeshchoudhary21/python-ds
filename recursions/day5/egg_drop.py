#classic egg drop problem
import sys


def egg_drop(e,f):
    if f==0 or f==1: return f
    if e==1: return f # worst case u know at top floor

    ans = sys.maxsize

    for k in range(1,f):
        temp = max(egg_drop(e-1,k),egg_drop(e,f-k-1))
        ans = min(ans,temp)

    return ans+1

eggs = 3
floor = 14
print(egg_drop(eggs,floor))
