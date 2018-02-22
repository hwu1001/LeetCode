# https://leetcode.com/problems/single-number/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Remember that for a given integer A, A XOR A will result in 0
        # So by XOR'ing all the pairs we'll simply be left with the single
        # number in the end since the pairs cancel each other out (resulting in 0)
        # and 0 XOR any integer will result in that integer
        res = 0
        for num in nums:
            res ^= num
        return res

if __name__ == "__main__":
    obj = Solution()
    arr = [1,7,5,1,6,5,6]
    print(obj.singleNumber(arr))