# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    # Time: O(n + (m * n)) - where n is the number of stones and m is the number of jewels
    # Space: O(1)
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # return sum(map(J.count, S))
        return sum(s in J for s in S)

if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    obj = Solution()
    print(obj.numJewelsInStones(J, S))