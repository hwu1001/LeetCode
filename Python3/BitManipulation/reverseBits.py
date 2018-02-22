# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    # @param n, an integer
    # @return an integer

    # String solution
    # Time: O(1) - In this solution we're creating a new
    #              binary string we create a string 32 characters in length
    #              and reverse it
    # Space: O(n) - where n is the number of digits
    def reverseBits(self, n):
        # Using the format function we turn the number given into binary with 32 character padding with '0'
        # as the pad character. Reverse it, then convert that into an int rather than a string
        return int(format(n, '032b')[::-1], 2)
    
    # Time: O(1) - Since it's a 32-bit integer the time will always require a loop
    #              of the same length (32 times once for each bit)
    # Space: O(1)
    def reverseBits2(self, n):
        ret = 0
        # The following takes from the back bit of n and puts it to the front of ret
        # << 1 will put a 0 at the end of ret. The n & 1, turns the last bit of n to
        # either a 1 or a 0, then the | will allow us to put that on the end of ret.
        # Then shift to the next bit on n by removing the last bit (>> 1)
        for _ in range(32):
            ret <<= 1
            ret |= n & 1
            n >>= 1
        return ret

if __name__ == "__main__":
    # For whatever reason reverseBits seems to be significantly faster than reverseBits2
    # Probably because format() is just C under the hood and the bit manipulation is all Python
    # import timeit
    # print(timeit.timeit("obj.reverseBits2(43261596)", setup="from __main__ import Solution; obj=Solution()"))
    obj = Solution()
    print(obj.reverseBits(43261596))
    