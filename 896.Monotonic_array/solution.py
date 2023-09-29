class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = True
            if nums[i] < nums[i-1]:
                dec = True
        return False if inc and dec else True
