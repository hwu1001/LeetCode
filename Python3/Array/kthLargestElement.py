# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq
from random import randint

class Solution:
    # Heapq solution
    # Time: O(nlogk)
    # Space: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return 0 
        h = []
        for n in nums:
            if len(h) + 1 > k:
                heapq.heappushpop(h, n)
            else:
                heapq.heappush(h, n)
        return h[len(h) - k]

    # Time: Best case O(n), worst case O(nlogn)
    # Space: O(n)
    def findKthLargestSort(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return 0
        return sorted(nums)[len(nums) - k]

    # Time: Best case is O(n), worst case O(n^2)
    # Space: O(1)
    def findKthLargestRandQuickSelect(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            ri = randint(l, r) # can also just shuffle the input instead
            nums[r], nums[ri] = nums[ri], nums[r]
            for i, v in enumerate(nums[l: r+1], l):
                if v >= nums[r]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l - 1

        if not nums or k < 1 or k > len(nums):
            return 0

        l, r, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]

if __name__ == "__main__":
    # l = [3,2,1,5,6,4]
    l = [3,2,3,1,2,4,5,5,6]
    k = 4
    obj = Solution()
    ans = obj.findKthLargestSort(l, k)
    print(ans)