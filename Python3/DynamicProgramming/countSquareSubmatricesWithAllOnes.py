# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List

class Solution:
    # Similar to maximal square
    # Time: O(mn) - where m is number of rows, n is number of elements in a row
    # Space: O(1) - Can update the grid in place, if not then O(n)
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] > 0 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                ans += matrix[i][j]
        return ans

if __name__ == '__main__':
    obj = Solution()
    m = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]
    # [
    #   [0,1,1,1],
    #   [1,1,2,2],
    #   [0,1,2,3]
    # ]
    assert(obj.countSquares(m) == 15)
    m2 = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
        ]
    # [
    #   [1,0,1],
    #   [1,1,0],
    #   [1,2,0]
    # ]
    assert(obj.countSquares(m2) == 7)