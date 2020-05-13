# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List

class Solution:
    # Binary search
    # Time: O(logn)
    # Space: O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0 # low expected to always be beginning of a pair
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            # The reason for this next line is that if, say, the entire array nums was pairs of numbers
            # it would be expected that at each positive index the next index would have that
            # number's pair. If it was an odd index it would mean the pair was one index before it
            # e.g., 1, 1, 2, 2 => (0, 1, 2, 3)
            # If we find the pair it means the single number has to be to the right since the current
            # pair along with the rest of the numbers will not all create pairs. Otherwise, the
            # single number is to the left because the pair check missed so it means the single number
            # offset our usual count by one and has to be to the left
            compare = mid + 1 if mid % 2 == 0 else mid - 1
            if nums[mid] == nums[compare]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

if __name__ == '__main__':
    obj = Solution()
    assert(obj.singleNonDuplicate([1,1,3]) == 3)
    assert(obj.singleNonDuplicate([1,3,3]) == 1)
    assert(obj.singleNonDuplicate([1,1,3,4,4]) == 3)
    assert(obj.singleNonDuplicate([1,1,3,3,4]) == 4)
    assert(obj.singleNonDuplicate([4,4,5,5,10,10,11,12,12]) == 11)
    assert(obj.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2)
    assert(obj.singleNonDuplicate([3,3,7,7,10,11,11]) == 10)
    assert(obj.singleNonDuplicate([3,3,7,7,10,10,11]) == 11)
    assert(obj.singleNonDuplicate([3,7,7,10,10,11,11]) == 3)
    assert(obj.singleNonDuplicate([1,1,2,2,3,3,4,4,5,5,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]) == 6)