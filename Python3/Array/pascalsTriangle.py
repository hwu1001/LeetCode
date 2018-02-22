# https://leetcode.com/problems/pascals-triangle/description/

from math import factorial
class Solution:
    # Time: O(n!)? or some exponent of n
    # Space: O(numRows ^ 2)
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # This method uses the formula for calculating a binomial coefficient at each cell of Pascal's triangle. It's not very
        # efficient since it uses factorial and does so in an inefficient manner
        return [[int((factorial(num)) / (factorial(i) * factorial(num - i))) for i in range(num + 1)] for num in range(0, numRows)]

    # Time: O(numRows ^ 2)
    # Space: O(numRows ^ 2)
    def generateDynProg(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        pascalsTri = [[1]]
        if numRows == 1:
            return pascalsTri
        for num in range(1, numRows):
            # For each row in the triangle they start and end with 1, otherwise we can use dynamic programming to calculate
            # the value
            pascalsTri.append([1,])
            pascalsTri[num].extend([(pascalsTri[num - 1][i - 1] + pascalsTri[num - 1][i]) for i in range(1, num)])
            pascalsTri[num].append(1)
        return pascalsTri

if __name__ == "__main__":
    obj = Solution()
    print(obj.generateDynProg(5))

