# https://leetcode.com/problems/contiguous-array/

from typing import List

class Solution:
    # Time: O(n)
    # Space: O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        m = {0: -1}
        max_len = 0
        count = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in m:
                max_len = max(max_len, i - m[count])
            else:
                m[count] = i
        return max_len

if __name__ == '__main__':
    obj = Solution()
    assert(obj.findMaxLength([0,1,0]) == 2)
    assert(obj.findMaxLength([0,1]) == 2)
    assert(obj.findMaxLength([0,0,0,1,1,1,1]) == 6)
    assert(obj.findMaxLength([0,1,1,0,1,1,1,0]) == 4)
    assert(obj.findMaxLength([0,1,0,0,1,1,0]) == 6)