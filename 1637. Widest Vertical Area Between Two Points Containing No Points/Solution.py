class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        _max=0
       
        for i in range(1,len(points)):
            _max=max(_max,points[i][0]-points[i-1][0])
        return _max
