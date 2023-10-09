class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''temp = 0
        ans = []
        for i in range(0,len(nums)):
            if nums[i] == target and temp == 0:
                ans.append(i)
                temp = 1
            if nums[i] != target and temp == 1:
                ans.append(i-1)
                break
        if len(ans) == 0:
            ans = [-1,-1]
        return ans'''
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]
