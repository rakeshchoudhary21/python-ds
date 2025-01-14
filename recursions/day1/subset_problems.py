

# print all subets of given set, works fine for unique sets
# ex: [1,2,3] => [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]

def all_subsets(input_list, index, temp:list):
    # to avoid duplicates from printing, we could use a list of lists and check if current temp is already there
    print(temp)
    for i in range(index, len(input_list)):
        temp.append(input_list[i])
        all_subsets(input_list, i + 1, temp)
        temp.remove(input_list[i])


# be careful with the input types in python :( make habit to declare them explicitly
def all_subsets_of_str(inputStr: str,temp:str,i):
    print(temp)
    for j in range(i, len(inputStr)):
        temp += inputStr[j]
        all_subsets_of_str(inputStr,temp,j+1)
        temp = temp[0:-1]

input_var = [1, 1, 3]
res = []
all_subsets(input_var, 0, [])
print(res)

#---- driver for the str subset problem
input_str = "ab"
all_subsets_of_str(input_str,"",0)

# besides the above approach there is also an input->output approach where we
