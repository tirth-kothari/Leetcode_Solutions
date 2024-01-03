class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        temp = 0
        for i in range(0,len(bank)):
            temp1 = bank[i].count('1')
            if temp1>0:
                prod = temp * temp1
                temp = temp1
                ans+=prod
        return ans
