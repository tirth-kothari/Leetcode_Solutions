class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [1 for i in xrange(len(s) + 1)]
        for i in xrange(1, len(s)):
            dp[i + 1] = (dp[i] if s[i] != '0' else 0) + (dp[i - 1] if 10 <= int(s[i-1] + s[i]) <= 26 else 0)
        return dp[-1]
