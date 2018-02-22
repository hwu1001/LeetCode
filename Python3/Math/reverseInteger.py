# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    # We're assuming we can only handle 32-bit signed ints here
    # String solution
    # Time: O(n)
    # Space: O(1)
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = None
        s = str(x)
        if x < 0:
            ret = int("-" + s[1:][::-1])
        else:
            ret = int(s[::-1])
        # 2 ^ 31 - 1 is the largest signed 32-bit int
        if ret > 2147483647 or ret < -2147483648:
            return 0
        else:
            return ret
    
    # Math solution
    # Time: O(log(n))
    # Space: O(1)
    def reverse2(self, x):
        if x < 0:
            # In Python the modulo operator always returns a number
            # the same sign as the denominator
            # https://stackoverflow.com/questions/3883004/negative-numbers-modulo-in-python
            return self.reverse2(-x) * -1
        rev = 0
        while(x != 0):
            rev = rev * 10 + x % 10
            x = x // 10 # need to do floor division for Python otherwise it will return a float
            if (rev > 2147483647 or rev < -2147483648):
                return 0
        return rev

if __name__ == "__main__":
    obj = Solution()
    print(obj.reverse2(120))
    print(obj.reverse2(-123))
    print(obj.reverse2(123))
    print(obj.reverse2(1534236469)) # Should return 0

        