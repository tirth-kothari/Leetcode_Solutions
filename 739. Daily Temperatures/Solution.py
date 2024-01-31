from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n  # Initialize the result list with zeros

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if ans[j] > 0:
                    j += ans[j]
                else:
                    break

            if j < n and temperatures[j] > temperatures[i]:
                ans[i] = j - i

        return ans
