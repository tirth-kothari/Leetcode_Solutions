class Solution:
    def minSteps(self, s, t):
        s , t = Counter(s) , Counter(t)
        return sum([ s[k]-t[k] for k in s if s[k]>t[k] ])
