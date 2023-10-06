class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        string = str(x)
        temp1,temp2 = [],[]
        ans = ""
        if string[0] == "-":
            for i in range(1,len(string)):
                temp1.append(string[i])
            temp2 = temp1[::-1]
            ans = ans + "-"
        else:
            for i in range(0,len(string)):
                temp1.append(string[i])
            temp2 = temp1[::-1]
        for i in temp2:
            ans = ans + i
        if int(ans) > MAX: return 0
        elif int(ans) < MIN: return 0
        else: return int(ans)
