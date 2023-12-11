class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        tar = int((0.25)*l)
        #print(l)
        #print(tar)
        s = set(arr)
        for i in s:
            x = arr.count(i)
            if x > tar:
                return i
