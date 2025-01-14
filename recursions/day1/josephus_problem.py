

# @description:: at each turn the kth person from current index is killed off, at last we need to tell which men survives

def josephus(men:list, k, current_index):
    if len(men)==1: print(men)
    else:
        current_index = (current_index + k-1) % len(men)

        del men[current_index] # remove is remove by value, use del instead
        josephus(men, k, current_index)


men = [1,2,3,4,5,6,7]
josephus(men, 3, 0)