class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                prod = (nums[i]-1)*(nums[j]-1)
                if prod>ans:
                    ans = prod
        return ans
