# https://leetcode.com/problems/unique-paths/description/

class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    # Dynamic programming solution filling entire grid
    # In the DP solution note that for a given cell that's not on the border,
    # in order to get to the route of that cell you either had to move from above it
    # or from the left of it. So to get the paths in a grid of 3 x 3, it will be the sum
    # of all the paths to get to 2 x 3 plus all the paths to get to 3 x 2.
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1] * n for i in range(m)]
        for rowIndex in range(1, m):
            for colIndex in range(1, n):
                grid[rowIndex][colIndex] = grid[rowIndex - 1][colIndex] + grid[rowIndex][colIndex - 1]
        return grid[m - 1][n - 1]

    # Time: O(m * n)
    # Space: O(min(m, n))
    # Dynamic programming solution updating a single row
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths2(n, m)
        paths = [1] * m
        for _ in range(1, n):
            for i in range(1, m):
                paths[i] += paths[i - 1]
        return paths[m - 1]

    # Time: O(min(m, n) * 2 - 3) - See the combination forumula below
    # Space: O(1)
    # Combination formula solution
    # http://www.mathwords.com/c/combination_formula.htm
    # For n choose r, the formula is n! / r! * (n - r)!, which is equal to
    # n(n-1)(n-2)...(n-r+1) / r! (the formula seen below)
    # Watch tutorial here: https://www.youtube.com/watch?v=M8BYckxI8_U
    def uniquePaths3(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        stepsDown = m - 1
        stepsRight = n - 1
        if stepsDown > stepsRight:
            stepsDown, stepsRight = stepsRight, stepsDown
        totalSteps = stepsDown + stepsRight
        numerator = denominator = 1
        for i in range(totalSteps, stepsRight, -1):
            numerator *= i
        for i in range(stepsDown, 1, -1):
            denominator *= i
        return int(numerator / denominator)

if __name__ == "__main__":
    obj = Solution()
    print(obj.uniquePaths3(3, 7))





