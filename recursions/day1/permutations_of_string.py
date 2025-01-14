

# given a string abc, print all its permutations
def permutations(str,index):
    if index == len(str):
        print(str)

    for i in range(index, len(str)):
        str = swap(str,index,i)
        permutations(str,index+1)
        str = swap(str,index,i)

def swap(str,i,j):
    sList = list(str)
    sList[i], sList[j] = sList[j], sList[i]
    return ''.join(sList)

# another problem could be permutations with case change or insert a space: abc=> abc, a_bc, a_b_c, ab_c
# use this input->output method in this case, much more intuitive
# replace the underscore with space for that variant of same problem

def permutations_with_underscore(inputStr, out,index):
    if len(inputStr) == 0:
        print(out) # use a map here to avoid duplicates
    else:
        # case 1: include an underscore at index
        case_1 = out
        if len(out)>0: case_1+= "_" # to avoid adding underscore before start of string
        case_1 += inputStr[0]
        # case 2: dont include an underscore at index
        case_2 = out+inputStr[0]

        # now call both branches
        permutations_with_underscore(inputStr[1:],case_1,index+1)
        permutations_with_underscore(inputStr[1:],case_2,index+1)


permutations("abc",0)
permutations_with_underscore("abc","",0)