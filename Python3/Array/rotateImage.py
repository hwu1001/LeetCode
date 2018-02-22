# https://leetcode.com/problems/rotate-image/description/

class Solution:
    # Time: O(n ^ 2)
    # Space: O(1) - Matrix is altered in place
    # Cyclic rotation - I don't recommend this solution, but this is the one
    # I implemented first
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        count = 0
        start = (0, 0)
        rowShift = 0
        colShift = 0
        # squares = n // 2
        # We know there are n * n points in the matrix so we will eventually need to move
        # each one (except in odd sized squares since the center won't move)
        while (count < n * n):
            row = start[0]
            col = start[1]
            prev = matrix[row][col]
            # For any given starting point we'll move four times, since there's four
            # corners in a square
            for i in range(4):
                if i == 0:
                    row = colShift
                    col = (n - 1) - rowShift
                elif i == 1:
                    row = (n - 1) - rowShift
                    col = (n - 1) - colShift
                elif i == 2:
                    row = (n - 1) - colShift
                    col = rowShift
                else:
                    row = rowShift
                    col = colShift
                temp = matrix[row][col]
                matrix[row][col] = prev
                prev = temp
                count += 1
            colShift += 1
            # If we meet this condition we've completed a square,
            # so move inwards in the matrix to the next square
            if (colShift == n - 1 - rowShift):
                rowShift += 1
                colShift = rowShift
            start = (rowShift, colShift)
        return
    
    # Time: O(n ^ 2)
    # Space: O(1)
    # Same as zip and list comprehension solutions below, but done
    # without the Python-specifics
    def rotate2(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    # Time: O(n ^ 2)
    # Space: O(n ^ 2) - since we're taking a list slice
    def rotateWithZip(self, matrix):
        # Reverse the matrix, then take vertical slices as new rows
        # clockwise rotate
        # first reverse up to down, then swap the symmetry 
        # 1 2 3     7 8 9     7 4 1
        # 4 5 6  => 4 5 6  => 8 5 2
        # 7 8 9     1 2 3     9 6 3
        matrix[:] = map(list, zip(*matrix[::-1]))
        return
    
    # Time: O(n ^ 2)
    # Space: O(n ^ 2) - since we're taking a list slice
    # Same as zip solution, but using list comprehension
    def rotateListComprehension(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        return
    
    # Left the counter-clockwise ones for reference
    # Time: O(n ^ 2)
    # Space: O(1)
    def rotateCounterClockwise(self, matrix):
        # anticlockwise rotate
        # first reverse left to right, then swap the symmetry
        # 1 2 3     3 2 1     3 6 9
        # 4 5 6  => 6 5 4  => 2 5 8
        # 7 8 9     9 8 7     1 4 7
        for row in matrix:
            row.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Time: O(n ^ 2)
    # Space: O(n ^ 2)
    def rotateCounterClockwiseListComprehension(self, matrix):
        # The first range is used to get the negative numbers necessary for the row to be
        # reversed.
        matrix[:] = [[row[i] for row in matrix] for i in range(len(matrix) - 1, -1, -1)]
        return

    # Time: O(n ^ 2)
    # Space: O(n ^ 2)
    def rotateCounterClockWiseZip(self, matrix):
        matrix[:] = map(list, zip(*[row[::-1] for row in matrix]))
        return

if __name__ == "__main__":
    obj = Solution()
    four = [ 
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    three = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    two = [[1,2], [3,4]]
    one = [[1]]
    five = [
        [1,1,1,1,1],
        [2,2,2,2,2],
        [3,3,3,3,3],
        [4,4,4,4,4],
        [5,5,5,5,5]
    ]
    six = [
        [1,1,1,1,1,1],
        [2,2,2,2,2,2],
        [3,3,3,3,3,3],
        [4,4,4,4,4,4],
        [5,5,5,5,5,5],
        [6,6,6,6,6,6]
    ]
    obj.rotateCounterClockwiseListComprehension(four)
    for row in four:
        print(row)
