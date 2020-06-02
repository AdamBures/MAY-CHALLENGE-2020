from itertools import chain

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        # DP[y][x] denotes the largest edge length of square, whose bottom right point is [y][x]
        dp_table = [ list(row) for row in matrix ]
        
        h, w = len(matrix), len(matrix[0])
        
        # Visit each matrix cell, except for row_0 and column_0
        for y in range(1, h):
            for x in range(1, w):
                
                if matrix[y][x]:
                    
                    # Make sure matrix[y][x] is 1, thus square can cover current matrix cell.
                    # Update largest edge length of sqaure, whose bottom right point is [y][x]
                    
                    dp_table[y][x] = 1 + min(dp_table[y][x-1],dp_table[y-1][x-1],dp_table[y-1][x])
        
        return sum( chain(*dp_table) )
