class Solution:

    def minCost(self, c: str, t: List[int]) -> int:
                
        cost = 0
        left = 0
        right = 1
        while True:

            if right == len(c):
                break
            
            if c[left]==c[right]:
                if t[left] <= t[right]:
                    cost += t[left]

                elif t[right] < t[left]:
                    cost += t[right]
                    right += 1
                    continue
        
            if (right-left)>1:
                left = right
                right += 1 
            else:
                left += 1
                right += 1

        return cost
