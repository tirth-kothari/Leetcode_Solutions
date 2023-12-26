class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        '''
        n dice

        k - 1 to 30

        '''
        MOD = 10 ** 9 + 7
        

        @cache 
        def calc(n, total):
            if total > target:
                return 0
            
            if n == 0:
                return int(total == target)

            best = 0

            for i in range(1, k + 1):
                best += calc(n - 1, total + i)

            return best % MOD





        return calc(n, 0) % MOD
