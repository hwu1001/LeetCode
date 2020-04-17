# https://leetcode.com/problems/minimum-path-sum/

from typing import List
from heapq import heappop, heappush

class Solution:
    # Time: O(m * n) - where m is the number of rows and n is the length of the rows
    # Space: O(n) - storing one row at a time
    def minPathSum(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [0] + [float('inf')] * (n - 1)
        for row in range(m):
            dp[0] += grid[row][0]
            for col in range(1, n):
                dp[col] = min(dp[col - 1], dp[col]) + grid[row][col]
        return dp[-1]
        
class Solution2:
    # Time: O(m * n) - where m is the number of rows and n is the length of the rows
    # Space: O(m * n) - altering the grid given (or could store it in new grid)
    def minPathSum(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for row in range (1, m):
            for col in range(1, n):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]


class Solution3:
    # Modified Dijkstra's algorithm - slower than DP for this problem
    # Time: O(m * n)
    # Space: O(m * n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        heap = [(grid[0][0], (0, 0))]
        visited = set()
        while heap:
            val, (row, col) = heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for r, c in [(row + 1, col), (row, col + 1)]:
                if r < len(grid) and c < len(grid[row]):
                    updated = val + grid[r][c]
                    heappush(heap, (updated, (r, c)))
                    if r == len(grid) - 1 and c == len(grid[row]) - 1:
                        return updated
        return val

if __name__ == '__main__':
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    obj = Solution()
    assert(obj.minPathSum(grid) == 7)
        