
# for a given N, print all N digit numbers which are in ascending order of digits
# ex: for N=2, 19 is ok to include but 20 cant be included, 21,22 also cant be included, next valid number is 23


def n_digit_asc(N, temp:list):
    if N==0:
        ans = 0
        for i in temp:
            ans = ans*10 +i
        print(ans)

    for i in range(10):
        if len(temp)==0 or temp[len(temp)-1]<i:
            temp.append(i)
            n_digit_asc(N-1, temp)
            temp.remove(i)


N = 2
n_digit_asc(2,[])