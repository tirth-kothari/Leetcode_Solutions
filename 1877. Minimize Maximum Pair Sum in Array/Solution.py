class Solution:
    def minPairSum(self, n: List[int]) -> int:
        m=0
        n.sort()
        j=len(n)-1
        for i in range(len(n)//2):
            x=n[i]+n[j]
            if x>m:
                m=x
            j=j-1
        return m
