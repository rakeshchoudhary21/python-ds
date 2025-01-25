
# description: https://leetcode.com/problems/elimination-game/description/
# basically start from left to right and eliminate first num and every alternate num, same logic for right to left then alternate between left and right.

def elimination_game(N):
     return L_R(N)


def L_R(N):
    if N==1: return 1
    else: return 2* R_L(int(N/2))

def R_L(N):
    if N==1: return 1

    if N%2==0: return 2* L_R(int(N/2))-1
    else: return 2* L_R(int(N/2))


input = [1,2,3,4,5,6,7,8,9]
print(elimination_game(9))