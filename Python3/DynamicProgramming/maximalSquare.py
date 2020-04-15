# https://leetcode.com/problems/maximal-square/

from typing import List

class Solution:
    # Time: O(mn) - where m is the number of rows, n is number of elements in a row
    # Space: O(n)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [0] * (cols + 1)
        max_sq_len = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(min(dp[j - 1], prev), dp[j]) + 1
                    max_sq_len = max(max_sq_len, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return max_sq_len * max_sq_len

if __name__ == '__main__':
    grid = [
        ['0', '1', '1', '1', '0'],
        ['1', '1', '1', '1', '0'],
        ['0', '1', '1', '1', '1'],
        ['0', '1', '1', '1', '1'],
        ['0', '0', '1', '1', '1']
    ]
    obj = Solution()
    assert(obj.maximalSquare(grid) == 9)