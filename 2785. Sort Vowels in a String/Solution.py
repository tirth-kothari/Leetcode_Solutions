VOWELS = 'AEIOUaeiou'
class Solution:
    def sortVowels(self, s: str) -> str:
        mapping = {x: i for i, x in enumerate(VOWELS)}
        occ = [0] * len(VOWELS)
        for ch in s:
            if ch in mapping: occ[mapping[ch]] += 1
        i = 0
        ans = []
        for ch in s:
            if ch in mapping:
                while occ[i] == 0: i += 1
                ans.append(VOWELS[i])
                occ[i] -= 1
            else: ans.append(ch)
        return ''.join(ans)
