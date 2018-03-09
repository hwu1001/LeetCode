# https://leetcode.com/problems/spiral-matrix/description/

class Solution(object):
    # Time: O(n)
    # Space: O(n)
    # Iterative solution - top right corner / bottom left corner
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        spiral = []
        rowStart = 0
        rowStop = len(matrix)
        colStart = 0
        colStop = len(matrix[0])
        numCells = rowStop * colStop
        while numCells > 0:
            # Print top right corner
            for i in range(colStart, colStop):
                spiral.append(matrix[rowStart][i])
                numCells -= 1
            for j in range(rowStart + 1, rowStop):
                spiral.append(matrix[j][colStop - 1])
                numCells -= 1
            colStop -= 1
            rowStart += 1
            if numCells <= 0:
                break
            # Print bottom left corner
            for i in range(colStop - 1, colStart - 1, -1):
                spiral.append(matrix[rowStop - 1][i])
                numCells -= 1
            # Because rowStop starts as the number of rows, need to decrease it
            # one more to skip the first number from the row we just appended above
            for j in range(rowStop - 1 - 1, rowStart - 1, -1):
                spiral.append(matrix[j][colStart])
                numCells -= 1
            colStart += 1
            rowStop -= 1
        return spiral

    # Time: O(n)
    # Space: O(n)
    # Iterative solution using a direction matrix
    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        if not matrix:
            return spiral
        spiral.extend(matrix[0])
        # Below are the [row, col] directions for movement
        # In order we're moving down rows, back through columns, up rows, forward through columns
        dirs = [[1,0], [0,-1], [-1,0], [0,1]]
        d = 0
        m = len(matrix)
        n = len(matrix[0])
        pos = [0, n - 1]
        i = (m - 1) * n # Minus one since we already took the top row
        while i > 0:
            for _ in range(1, m):
                i -= 1
                pos[0] += dirs[d][0]
                pos[1] += dirs[d][1]
                spiral.append(matrix[pos[0]][pos[1]])
            m -= 1 # Decrease the size of the row or column depending on mode
            m, n = n, m # Switch between going horizontal and vertical
            d = (d + 1) % 4 # Loop through direction offsets
        return spiral

if __name__ == "__main__":
    matrix = [[1,2,3], 
              [4,5,6], 
              [7,8,9]]
    
    # matrix = [[1,2,3,4],
    #           [5,6,7,8]]

    # matrix = [[1,2,3,4],
    #           [5,6,7,8],
    #           [9,10,11,12]]
    
    # matrix = [[1,2,3],
    #           [4,5,6],
    #           [7,8,9],
    #           [10,11,12]]
    
    # matrix = [[1,2],[3,4]]

    obj = Solution()
    print(obj.spiralOrder(matrix))
