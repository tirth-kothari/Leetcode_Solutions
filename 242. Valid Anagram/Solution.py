class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        l1[:0]=s
        l2[:0]=t
        if len(l1)==len(l2):
            for i in l2:
                if i in l1:
                    x=l1.index(i)
                    l1.pop(x)
            if len(l1)!=0:
                return False
            else:
                return True
        else:
            return False
