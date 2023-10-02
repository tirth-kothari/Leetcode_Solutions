class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        temp = 0
        ans = 0
        for i in range(0,len(player1)):
            if player1[i] == 10:
                if temp == 0:
                    ans = ans + player1[i]
                else:
                    ans = ans + (player1[i]*2)
                temp = 2
            elif temp == 2:
                ans = ans + (player1[i]*2)
                temp = temp-1
            elif temp == 1:
                ans = ans + (player1[i]*2)
                temp = temp-1
            else:
                ans = ans + player1[i]
        temp = 0
        ans2 = 0
        for i in range(0,len(player2)):
            if player2[i] == 10:
                if temp == 0:
                    ans2 = ans2 + player2[i]
                else:
                    ans2 = ans2 + (player2[i]*2)
                temp = 2
            elif temp == 2:
                ans2 = ans2 + (player2[i]*2)
                temp = temp-1
            elif temp == 1:
                ans2 = ans2 + (player2[i]*2)
                temp = temp-1
            else:
                ans2 = ans2 + player2[i]
        if ans>ans2:
            return 1
        elif ans2>ans:
            return 2
        else:
            return 0
