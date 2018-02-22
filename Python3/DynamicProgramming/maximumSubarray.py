# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        arrMax = localMax = nums[0]
        # Kadane's algorithm
        for val in nums[1:]:
            localMax = max(val, localMax + val)
            arrMax = max(arrMax, localMax)
        return arrMax

if __name__ == "__main__":
    # l = [-2,1,-3,4,-1,2,1,-5,4]
    l = [2,2,2,2,3,-11,10]
    # l = [-1,1,-2,1,-2,4]
    # l = [-1,-5,-2,-1]
    # l = [1,1,1,-3,1,1,2]
    obj = Solution()
    print(obj.maxSubArray(l))
