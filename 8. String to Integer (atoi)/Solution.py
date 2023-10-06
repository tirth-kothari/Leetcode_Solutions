class Solution:
    def myAtoi(self, s: str) -> int:
        '''ans=""
        temp = 1
        for i in s:
            #print(type(i))
            if i.isalpha():
                temp = 0
                if ans:
                    return ans
                else:
                    return 0
            if temp!=0:
                if i in ["-","+"]:
                    #print("here")
                    ans=ans+i
                    temp = 1
                #elif i in [0,1,2,3,4,5,6,7,8,9]:
                elif i in ["0","1","2","3","4","5","6","7","8","9"]:
                    #print("now")
                    ans = ans + i
                    temp=1
        print(type(ans))
        #print(ans,"ye")
        return int(ans)'''
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, 1  # empty denotes we have not seen any number, sign is -1 or 1
        for c in s:
            if empty:
                if c == ' ': continue  # ignore the leading whitespace
                elif c == '-': sign = -1  # final answer is a negative number
                elif c.isdigit(): n = int(c)  # the first digit of number
                elif c != '+': return 0  # the first char is not a digit and not in (' ', '+', '-'), so s is invalid
                empty = False  # the first char is a digit or '+' or '-', valid number starts
            else:
                if c.isdigit():
                    n = n * 10 + int(c)
                    if sign * n > MAX: return MAX
                    elif sign * n < MIN: return MIN
                else: break   # end of valid number
        return sign * n  # sign is 1 or -1 
