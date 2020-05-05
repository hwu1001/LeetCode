# https://leetcode.com/problems/number-complement/

class Solution:
    # Time: O(n) - where n is the number of bits in num
    # Space: O(1) - Since 32 bit integer, constant size of arr
    def findComplement(self, num: int) -> int:
        b = bin(num)
        ans = []
        for val in b[2:]:
            if val == '1':
                ans.append('0')
            else:
                ans.append('1')
        return int(''.join(ans), 2)

class Solution2:
    # Key part to remember here is that 0 XOR 1 is 1 and 1 XOR 1 is 0
    # Time: O(n)
    # Space: O(1)
    def findComplement(self, num: int) -> int:
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num

if __name__ == '__main__':
    obj = Solution2()
    # bin(5) => '0b101'
    # bin(2) => '0b10'
    assert(obj.findComplement(5) == 2)
    # bin(1) => '0b1'
    # bin(0) => '0b0'
    assert(obj.findComplement(1) == 0)