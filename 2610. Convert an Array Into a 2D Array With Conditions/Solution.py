class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        s = {}
        ans = []
        while len(nums)>0:
            s = set(nums)
            ans.append(list(s))
            for i in s:
                nums.remove(i)
        return ans
