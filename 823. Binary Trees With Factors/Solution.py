class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        for x in arr: dp[x] = 1
        for i, a in enumerate(arr):
            for j in arr[:i]:
                if a % j == 0 and a // j in dp:
                    dp[a] += dp[j] * dp[a//j]
        return sum(dp.values()) % (10**9+7)
