class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Check if the matrix is empty
        if not matrix:
            return 0
        
        n = len(matrix)
        
        # Start from the second row
        for i in range(1, n):
            for j in range(n):
                # Calculate the minimum falling sum for each element
                matrix[i][j] += min(
                    matrix[i-1][max(0, j-1)],
                    matrix[i-1][j],
                    matrix[i-1][min(n-1, j+1)]
                )
        
        # Find the minimum sum in the last row
        return min(matrix[-1])
