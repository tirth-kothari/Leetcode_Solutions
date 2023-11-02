class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        ans = 0
        temp1 = str(x)
        for i in temp1:
            if i == "1":
                ans+=1
        return ans
