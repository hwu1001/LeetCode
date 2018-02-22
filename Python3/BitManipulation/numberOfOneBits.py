# https://leetcode.com/problems/number-of-1-bits/description/
class Solution(object):
    # Time: O(log(n)) = O(32)
    # Space: O(1)
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")
    
    # Time: O(log(n)) = O(32)
    # Space: O(1)
    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            # The bitwise AND operator will flip the least-significant 1 bit to 0
            # Once the number becomes zero we know there are no more 1 bits
            # Another way we could do this is looping through all 32 bits and using
            # a bit mask that starts at binary representation of 1 and continuously 
            # shifts the 1 bit all the way to the end while using bitwise AND (&) on
            # the number given to see how many 1 bits there are.
            n &= (n - 1)
            sum +=1
        return sum

if __name__ == "__main__":
    obj = Solution()
    print(obj.hammingWeight2(11))