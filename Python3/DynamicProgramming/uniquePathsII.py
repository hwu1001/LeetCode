# https://leetcode.com/problems/unique-paths-ii/

from typing import List

class Solution:
    # Time: O(m * n) - where m is number of rows and n is length of a row 
    # Space: O(m * n) - or O(1)? if altering then given list is no additional space
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for col in range(1, n):
            if obstacleGrid[0][col] != 1:
                obstacleGrid[0][col] = obstacleGrid[0][col - 1]
            else:
                obstacleGrid[0][col] = 0
        for row in range(1, m):
            if obstacleGrid[row][0] != 1:
                obstacleGrid[row][0] = obstacleGrid[row - 1][0]
            else:
                obstacleGrid[row][0] = 0

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] != 1:
                    obstacleGrid[row][col] = obstacleGrid[row][col - 1] + obstacleGrid[row - 1][col]
                else:
                    obstacleGrid[row][col] = 0
        return obstacleGrid[m - 1][n - 1]

class Solution2:
    # Time: O(m * n)
    # Space: O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        dp = [0] * len(obstacleGrid[0])
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp[0] = 1
        for row in range(0, m):
            for col in range(0, n):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]
        return dp[-1]

if __name__ == '__main__':
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
        ]
    # grid2 = [[1]]
    obj = Solution2()
    print(obj.uniquePathsWithObstacles(grid))