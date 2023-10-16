class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        def getR1(self,rowIndex) -> List[int]:
            if rowIndex == 0:
                List=[]
                return List
            elif rowIndex == 1:
                List=[1]
                return List
            elif rowIndex == 2:
                List=[1,1]
                return List
            else:  
                ans=[]
                l1=getR1(self,(rowIndex-1))
                ans.append(1)
                for i in range(1,rowIndex-1):
                    ans.append(l1[i-1]+l1[i])
                ans.append(1)
                return ans
        return getR1(self,rowIndex)
