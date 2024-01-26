class Solution:
    def findPaths(self, m, n, N, x, y):
        M = [[0 for i in range(n)] for j in range(m)]
        for _ in range(N):
            M = [[(i == 0 or M[i - 1][j]) + (i + 1 == m or M[i + 1][j])
                  + (j == 0 or M[i][j - 1]) + (j + 1 == n or M[i][j + 1])
                  for j in range(n)] for i in range(m)]
        return M[x][y] % (10 ** 9 + 7)
