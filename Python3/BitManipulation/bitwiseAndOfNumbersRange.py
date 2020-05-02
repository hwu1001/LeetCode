# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Question can also be thought of as finding the common prefix
# of m and n when they have the same binary length

class Solution:
    def findMsbPos(self, n: int) -> int:
        msb_p = -1
        while n > 0:
            n >>= 1
            msb_p += 1
        return msb_p

    # Time: O(n - m) ? - Finding msb count as n?
    # Space: O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        while m > 0 and n > 0:
            msb_m = self.findMsbPos(m)
            msb_n = self.findMsbPos(n)
            if msb_m != msb_n:
                break
            msb_val = 1 << msb_m
            ans += msb_val # equivalent to 2^msb_m added to ans
            m -= msb_val
            n -= msb_val
        return ans

class Solution2:
    # Time: O(n * 32)
    # Space: O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i

class Solution3:
    # Time: O(n * 32)
    # Space: O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= n-1
        return m & n

class Solution4:
    # Time: O(n * 32)
    # Space: O(1)
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        # Looking for where the common prefix ends
        for bit in range (30, -1, -1):
            if (m & (1 << bit)) != (n & (1 << bit)):
                break
            else:
                # If there is a common prefix then it will be in the answer
                ans |= (m & (1 << bit))
        return ans

if __name__ == '__main__':
    obj = Solution4()
    assert(obj.rangeBitwiseAnd(5, 7) == 4)
    assert(obj.rangeBitwiseAnd(0,1) == 0)
