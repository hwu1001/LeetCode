# This problem is from a monthly challenge

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:
from typing import List

# Implemented anyways so I can test it locally
class BinaryMatrix:
    def __init__(self, grid: List[List[int]]):
        self.mat = grid
    
    def get(self, x: int, y: int) -> int:
        return self.mat[x][y]

    def dimensions(self) -> List[int]:
        return [len(self.mat), len(self.mat[0])]

class Solution:
    # Time: O(logn) - Only have to search half the matrix at most
    # Space: O(1) - Just need the input matrix
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        left_most = -1
        row = 0
        # Start at top right
        for col in range(n - 1, -1, -1):
            while row < m:
                # If a 1 is found move to the next col (left)
                if binaryMatrix.get(row, col) == 1:
                    left_most = col
                    break
                # Otherwise move down (to the next row)
                row += 1 
        return left_most


if __name__ == '__main__':
    obj = Solution()
    mat1 = [
        [0,0,0,1],
        [0,0,1,1],
        [0,1,1,1]
    ]
    assert(obj.leftMostColumnWithOne(BinaryMatrix(mat1)) == 1)
    mat2 = [
        [0,0],
        [0,1]
    ]
    assert(obj.leftMostColumnWithOne(BinaryMatrix(mat2)) == 1)
    mat3 = [[0,0],[0,0]]
    assert(obj.leftMostColumnWithOne(BinaryMatrix(mat3)) == -1)
    mat4 = [
        [0,0],
        [1,1]
    ]
    assert(obj.leftMostColumnWithOne(BinaryMatrix(mat4)) == 0)