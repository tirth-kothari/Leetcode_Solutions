class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        dic =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        def helper(arr):
            count = 0
            for c in arr:
                if c in dic:
                    count += 1
            return count
        
        l = len(s)//2
        return helper(s[:l]) == helper(s[l:])
