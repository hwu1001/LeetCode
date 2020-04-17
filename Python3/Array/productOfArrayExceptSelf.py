# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    # Time: O(n) - two passes across the list of nums
    # Space: O(1) - It's O(n) if you count the value we have to return
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        return ans

if __name__ == '__main__':
    obj = Solution()
    assert(obj.productExceptSelf([1,2,3,4]) == [24, 12, 8, 6])