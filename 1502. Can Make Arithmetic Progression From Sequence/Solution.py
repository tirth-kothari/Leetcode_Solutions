class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr)<2:
            return True
        else:
            for i in range(1,len(arr)-1):
                if arr[i]-arr[i-1]==arr[i+1]-arr[i]:
                    pass
                else:
                    return False
            return True
