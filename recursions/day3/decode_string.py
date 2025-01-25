

def decode(s):
    nums = []
    chars = []
    res=""
    i = 0
    while i<len(s):
        c = s[i]

        if c.isnumeric():
            # we can potentially have multi digit numbers??
            num = 0
            while s[i].isnumeric():
                num = num*10 + int(s[i])
                i+=1
            nums.append(num)

        elif c=='[':
            chars.append(res)
            res = ""
            i+=1
        elif c==']':
            res = chars.pop()+ res * nums.pop()
            i+=1
        else:
            res+=c
            i+=1


    print(res)


decode('3[A]29[BC]')