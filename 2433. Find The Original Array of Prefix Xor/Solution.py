class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        '''
        C XOR (C XOR num2) = num2
        '''
        prev = pref[0]
        res = [prev]
        for i in pref[1:]:
            res.append(prev^i)
            prev = i
        return res
