# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    # Time: O(n)
    # Space: O(n)
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set(nums)
        return len(numSet) != len(nums)

if __name__ == "__main__":
    obj = Solution()
    print(obj.containsDuplicate([1,2,3,4,5]))