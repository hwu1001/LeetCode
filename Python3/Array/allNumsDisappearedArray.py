# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List

class Solution:
    # Time: O(n)
    # Space: O(1) - Editing the input array of numbers
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        count = 0
        if not nums:
            return ret
        while count < len(nums):
            val = abs(nums[count]) - 1
            if (nums[val] > 0):
                nums[val] = -nums[val]
            count += 1
        for i, val in enumerate(nums):
            if val > 0:
                ret.append(i + 1)
        return ret

if __name__ == "__main__":
    obj = Solution()
    assert(obj.findDisappearedNumbers([3,1,1]) == [2])
    assert(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6])
        