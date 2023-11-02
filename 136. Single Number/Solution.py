class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.append(i)
        #print(ans)
        return ans[0]
