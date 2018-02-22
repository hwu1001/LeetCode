# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    # Time: O(n)
    # Space: O(1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        # When we start the loop below at 3, the ways to get to stair 1 is 1,
        # the ways to get to stair 2 is 2. The ways to get to stair n is the 
        # sum of the ways to get to stair (n - 1) and stair (n - 2).
        twoStairsDown = 1
        oneStairDown = 2
        for _ in range(3, n):
            twoStairsDown, oneStairDown = oneStairDown, (twoStairsDown + oneStairDown)
        return (twoStairsDown + oneStairDown)

if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(3))
