from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
      #the below commented code gives correct output but TLE.
        '''ans = []
        stop = len(nums)-k+1
        for i in range(0,stop):
            temp_number=0
            temp1=nums[i:i+k]
            temp1.sort()
            temp_number = temp1[x-1]
            if temp_number<0:
                ans.append(temp_number)
            else:
                ans.append(0)
        return ans'''
        ans = []
        n = len(nums)
        sl=SortedList()
        for i in range(n):
            sl.add(nums[i])
            
            if i-k>=0:
                sl.remove(nums[i-k])
                #print(sl,"when deleted")
                
            if len(sl)>=k:
                #print(sl)
                t=sl[x-1]
                if t>=0:
                    ans.append(0)
                else:
                    ans.append(t)
        return ans
