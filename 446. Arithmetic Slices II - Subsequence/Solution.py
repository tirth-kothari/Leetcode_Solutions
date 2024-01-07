class Solution:
    def numberOfArithmeticSlices(self, A):
        dp = defaultdict(int)
        for i in reversed(range(len(A))):
            for j in range(i+1, len(A)):
                if (j, A[j]-A[i]) in dp:
                    dp[i, A[j]-A[i]] += dp[j, A[j]-A[i]]
                dp[i, A[j]-A[i]] += 1
        return sum(dp.values())-len(A)*(len(A)-1)//2
