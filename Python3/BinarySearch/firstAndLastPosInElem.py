# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        left_ndx = self.binarySearch(nums, target, True)
        # condition must be in this order, otherwise could get index out of range error
        if left_ndx == len(nums) or nums[left_ndx] != target:
            return [-1 , -1]
        return [left_ndx, self.binarySearch(nums, target, False) - 1]
    
    def binarySearch(self, nums: [int], target: int, search_left: bool) -> int:
        low = 0
        # this can't have - 1 because we're subtracting one in searchRange
        # Ex: for input [1], 1 we don't want to return [0, -1]
        high = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target or (search_left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    obj = Solution()
    assert(obj.searchRange([1], 1) == [0,0])
    assert(obj.searchRange([], 0) == [-1, -1])
    assert(obj.searchRange([1,2,5,5,5,9], 5) == [2,4])
    assert(obj.searchRange([5,7,7,8,8,10], 8) == [3,4])
    assert(obj.searchRange([5,7,7,8,8,10], 6) == [-1,-1])
