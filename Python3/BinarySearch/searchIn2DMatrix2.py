# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List

class Solution:
    # Time: O(logn) - Search half the matrix at most
    # Time: O(1) - No additional space other than the matrix to search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        # Start at top right and traverse diagonally to divide matrix
        for col in range(n - 1, -1, -1):
            while row < m:
                if matrix[row][col] == target:
                    return True
                # If current value is larger then move left
                if matrix[row][col] > target:
                    break
                # Otherwise move down
                row += 1
        return False

if __name__ == '__main__':
    m = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    obj = Solution()
    assert(obj.searchMatrix(m, 17) == True)
    assert(obj.searchMatrix(m, 5) == True)
    assert(obj.searchMatrix(m, 1) == True)
    assert(obj.searchMatrix(m, 18) == True)
    assert(obj.searchMatrix(m, 30) == True)
    assert(obj.searchMatrix(m, 31) == False)
    assert(obj.searchMatrix(m, 25) == False)

