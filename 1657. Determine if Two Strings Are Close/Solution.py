class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        d1 = dict()
        d2 = dict()

        for i in word1:
            if i in d1:
                d1[i]=d1[i]+1
            else:
                d1[i] = 1
        for j in word2:
            if j in d2:
                d2[j]=d2[j]+1
            else:
                d2[j]=1
        return (set(word1)==set(word2) and (sorted(d1.values())==sorted( d2.values())))
