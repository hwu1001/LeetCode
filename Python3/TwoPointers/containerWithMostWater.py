# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    # Time: O(n)
    # Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while start != end:
            min_height = min(height[start], height[end])
            container_len = end - start
            max_area = max(max_area, min_height * container_len)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return max_area

if __name__ == "__main__":
    l = [1,8,6,2,5,4,8,3,7]
    obj = Solution()
    assert(obj.maxArea(l) == 49)