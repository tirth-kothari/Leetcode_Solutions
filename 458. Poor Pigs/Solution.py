class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = minutesToTest//minutesToDie+1
        lo, hi = 0, buckets
        while(lo<hi):
            mid = (hi+lo)//2
            if base**mid<buckets:
                lo = mid+1
            else:
                hi = mid
        return lo
