# https://leetcode.com/problems/hamming-distance/description/

class Solution:
    # Time: O(1)
    # Space: O(1)
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
    
    # Bit manipulation solution - how it would be seen in most other languages
    # Time: O(1)
    # Space: O(1)
    def hammingDistance2(self, x, y):
        dist = 0
        xor = x ^ y
        while xor:
            # The bitwise AND operator will flip the least-significant 1 bit to 0
            # Once the number becomes zero we know there are no more 1 bits
            dist += 1
            xor &= (xor - 1)
        return dist

if __name__ == '__main__':
    obj = Solution()
    x = 'this is a test'
    y = 'wokka wokka!!!'
    count = 0
    for i in range(len(x)):
        count += obj.hammingDistance(ord(x[i]), ord(y[i]))
    # Results in a score of 37. Thanks cryptopals!
    print(count)