# https://leetcode.com/problems/fizz-buzz/description/
class Solution:
    # Time: O(n)
    # Space: O(1)
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if (i % 3 == 0 and i % 5 == 0):
                res.append("FizzBuzz")
            elif (i % 3 == 0):
                res.append("Fizz")
            elif (i % 5 == 0):
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
