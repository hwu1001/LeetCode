# https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque

class Solution:
    def bfs(self, grid: List[List[str]], row: int, col: int):
        grid[row][col] = '0'
        q = deque()
        q.append((row, col))
        while q:
            r, c = q.popleft()
            if r + 1 < len(grid) and grid[r + 1][c] == '1': # down
                q.append((r + 1, c))
                grid[r + 1][c] = '0'
            if r - 1 >= 0 and grid[r - 1][c] == '1': # up
                q.append((r - 1, c))
                grid[r - 1][c] = '0'
            if c - 1 >= 0 and grid[r][c - 1] == '1': # left
                q.append((r, c - 1))
                grid[r][c - 1] = '0'
            if c + 1 < len(grid[r]) and grid[r][c + 1] == '1': # right
                q.append((r, c + 1))
                grid[r][c + 1] = '0'

    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    self.bfs(grid, row, col)
                    num_islands += 1
        return num_islands

    def dfs(self, grid: List[List[str]], row: int, col: int):
        if row >= 0 and row < len(grid) and col >=0 and col < len(grid[row]) and grid[row][col] == '1':
            grid[row][col] = '0'
            self.dfs(grid, row + 1, col) # down
            self.dfs(grid, row - 1, col) # up
            self.dfs(grid, row, col - 1) # left
            self.dfs(grid, row, col + 1) # right

    def numIslandsDfs(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    num_islands += 1
        return num_islands

if __name__ == '__main__':
    # grid = [ # 1
    #     ['1', '1', '1', '1', '0'],
    #     ['1', '1', '0', '1', '0'],
    #     ['1', '1', '0', '0', '0'],
    #     ['0', '0', '0', '0', '0']
    # ]
    grid = [ # 3
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    # grid = [["1","0","1","1","0","1","1"]] # 3
 
    # grid = [ # 2
        # ["1","0","1","1","0","1","1"],
        # ["1","0","0","1","0","0","0"],
        # ["1","1","1","1","0","0","0"]
    # ]

    # [["1","0","1","1","0","1","1"],["1","0","0","1","0","0","0"],["1","1","1","1","0","0","0"]] # 1
    # grid = [ # 1
    #     ['0', '0'],
    #     ['1', '0']
    # ]

    obj = Solution()
    print(obj.numIslandsDfs(grid))