# https://leetcode.com/problems/two-sum/description/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}
        for i, val in enumerate(nums):
            temp = target - val
            if temp in numsDict:
                return [numsDict[temp], i]
            else:
                numsDict[val] = i
        return []

if __name__ == "__main__":
    obj = Solution()
    # print(obj.twoSum([3,2,4], 6))
    print(obj.twoSum([2,7,11,15], 18))