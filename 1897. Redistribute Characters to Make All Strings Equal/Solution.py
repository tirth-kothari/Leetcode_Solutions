class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for i in words:
            for j in i:
                counts[j]+=1
         
        temp = len(words)
        for i in counts.values():
            if i%temp != 0:
                return False
        return True
