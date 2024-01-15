class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #loop through to find all numbers
        players = {}
        for match in matches:
            if match[0] not in players:
                players[match[0]]=0
            if match[1] not in players:
                players[match[1]]=1
            else:
                players[match[1]]+=1
        winnersLosers = [[],[]]
        for player in players:
            if players[player] == 0:
                winnersLosers[0].append(player)
            elif players[player] == 1:
                winnersLosers[1].append(player)
        winnersLosers[0].sort()
        winnersLosers[1].sort()

        return winnersLosers
