from functools import lru_cache

class Solution:
    def maxLength(self, arr: List[str]) -> int:
                
        def dfs(i, cur):
            if len(cur) != len(set(cur)):
                return 0
            
            max_len = len(cur)
            for j in range(i, len(arr)):
                max_len = max(dfs(j, cur + arr[j]), max_len)
            return max_len
            
        return dfs(0, "")
