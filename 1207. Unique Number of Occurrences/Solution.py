class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrMap = defaultdict(int)
        for e in arr:
            arrMap[e] += 1
        
        return len(arrMap) == len(set(arrMap.values()))
