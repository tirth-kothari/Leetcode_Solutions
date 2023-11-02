class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            ans = math.log(n)/math.log(2)
            #print(ans)
            ans = round(ans,12)
            #print(ans)
            if ans.is_integer():
                return True
            else:
                return False
