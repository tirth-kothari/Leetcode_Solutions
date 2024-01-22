class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        c = Counter(nums)
        arr = [0] * 2
        for i in range(1, N + 1):
            if c[i] == 2:
                arr[0] = i
            if c[i] == 0:
                arr[1] = i

        return arr
