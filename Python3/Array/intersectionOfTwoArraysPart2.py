# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

class Solution:
    # Time: O(n + m)
    # Space: O(n)
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        valCounter = {}
        for num in nums1:
            if num in valCounter:
                valCounter[num] += 1
            else:
                valCounter[num] = 1
        intersect = []
        for num in nums2:
            if num in valCounter and valCounter[num] > 0:
                intersect.append(num)
                valCounter[num] -= 1
        return intersect

if __name__ == "__main__":
    nums1 = [1,2,1,2]
    nums2 = [2]
    obj = Solution()
    print(obj.intersect(nums1, nums2))
