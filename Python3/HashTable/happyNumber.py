# https://leetcode.com/problems/happy-number/description/

class Solution:
    # Time: O(k) - Where k is the time until a cycle is found or
    #              the squared number sum equals 1
    # Space: O(k) - Where k is the number of numbers stored until a
    #               cycle is found or the squared number sum equals 1
    # Solution using string manipulation
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seenNums = {}
        while n != 1:
            digits = str(n)
            tempNum = 0
            for d in digits:
                tempNum += int(d)**2
            if tempNum in seenNums:
                return False
            else:
                seenNums[tempNum] = 1
            n = tempNum
        return True

    # Time: O(k) - Where k is the time until a cycle is found or
    #              the squared number sum equals 1
    # Space: O(k) - Where k is the number of numbers stored until a
    #               cycle is found or the squared number sum equals 1
    # Solution using remainders
    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seenNums = set()
        squareSum = 0
        remain = 0
        while n not in seenNums:
            seenNums.add(n)
            squareSum = 0
            while n > 0:
                remain = n % 10
                squareSum += remain * remain
                n //= 10 # In Python important floor division is used here
            if squareSum == 1:
                return True
            else:
                n = squareSum
        return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.isHappy2(28))