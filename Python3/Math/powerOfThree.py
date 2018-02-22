# https://leetcode.com/problems/power-of-three/description/
class Solution:
    # Time: O(log3(n)) - log base 3 that is. The number of divisions
    #                    is given by that logarithm
    # Space: O(1)
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
    
    # This one is a bit of an exploit of the problem, but seems worth noting
    # Due to the problem limiting the number to an integer of 32 bits the largest
    # number that can be checked is 2147483647 (2 ^ 31 - 1). 
    # So we can find the largest int that is a power of three:
    #   3 ^ (log3(maxInt)) = 3 ^ 19.56 = 3 ^ 19 = 1162261467
    # Since 3 is a prime only the divisors of 3^19 are 3^0, 3^1,...,3^19.
    # Time: O(1)
    # Space: O(1)
    def isPowerOfThreeHack(self, n):
        return n > 0 and 1162261467 % n == 0

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPowerOfThree(45))