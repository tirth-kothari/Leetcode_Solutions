class Solution:
    def minimumTotal(self, triangle):
        for i in range(1,len(triangle)):
            for j in range(i+1):
                temp1, temp2 = float(inf), float(inf)
                if j-1>=0:
                    temp1 = triangle[i-1][j-1]
                if j<i:
                    temp2 = triangle[i-1][j]
                triangle[i][j] = min(temp1, temp2)+triangle[i][j]
        return min(triangle[-1])
