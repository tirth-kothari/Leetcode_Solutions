class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        if n == 1:
            return 0
        while n>2:
            if n%2==0:
                n = n/2
                matches = matches + n
            else:
                matches = matches + (n//2)
                n = (n//2)+1
                #print(n)
        return int(matches+1)
