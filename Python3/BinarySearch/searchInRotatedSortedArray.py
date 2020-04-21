# 

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        # binary search for lowest value
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        rotated = low
        low = 0
        n = len(nums)
        high = n - 1
        # binary search for target
        while low <= high:
            mid = low + (high - low) // 2
            actual_mid = (mid + rotated) % n
            if target == nums[actual_mid]:
                return actual_mid
            if nums[actual_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            # target and mid are on the same side
            if ((nums[mid] - nums[-1]) * (target - nums[-1])) > 0:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            elif target > nums[-1]:
                high = mid # target on the left side
            else:
                low = mid + 1 # target on the right side
        if nums[low] == target:
            return low
        return -1

if __name__ == '__main__':
    obj = Solution2()
    print(obj.search([4,5,6,7,0,1,2], 6))