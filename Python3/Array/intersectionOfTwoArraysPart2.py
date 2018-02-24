# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

from collections import Counter

class Solution:
    # Time: O(m + n)
    # Space: O(min(m, n))
    # Hash map solution
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

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

    # Time: O(m + n)
    # Space: O(min(m, n))
    # Similar to Hash solution, but using collections.Counter object
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # The & operator on collections.Counter objects
        # results in the intersection
        # min(m[x], n[x])
        intersectCount = Counter(nums1) & Counter(nums2)
        return list(intersectCount.elements())
    
    # Time: O(m + n)
    # Space: O(n) - If sorting is not counted in space, then 
    #               just the return will be O(n). The sort for 
    #               arrays in Python is worst-case O(n)
    # Two pointers solution
    def intersect3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        ndx1 = 0
        ndx2 = 0
        intersect = []
        while ndx1 < len(nums1) and ndx2 < len(nums2):
            if nums1[ndx1] > nums2[ndx2]:
                ndx2 += 1
            elif nums1[ndx1] < nums2[ndx2]:
                ndx1 += 1
            else:
                intersect.append(nums1[ndx1])
                ndx1 += 1
                ndx2 += 1
        return intersect

if __name__ == "__main__":
    nums1 = [1,2,1,2]
    nums2 = [2,2]
    obj = Solution()
    print(obj.intersect(nums1, nums2))
