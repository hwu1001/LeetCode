# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    # Time: O(n)
    # Space: O(log(n)) - since we're sorting one of the arrays
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if (m == 0):
            nums1[:] = nums2
            return
        elif (n == 0):
            return
        else:
            nums1[m:] = nums2
            nums1.sort()
        return
    
    # Time: O(n)
    # Space: O(n)
    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while (m > 0 and n > 0):
            if (nums1[m - 1] > nums2[n - 1]):
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if (n > 0):
            # This operation is O(n) space because the list slice of
            # nums2 is held in memory for assignment.
            # https://stackoverflow.com/questions/4948293/python-slice-assignment-memory-usage
            nums1[:n] = nums2[:n]
        return

if __name__ == "__main__":
    obj = Solution()
    arr1 = [2,4,6,0,0,0,0]
    arr2 = [1,1,3,5]
    obj.merge2(arr1, 3, arr2, 4)
    print(arr1)
    # arr1 = [0]
    # arr2 = [1]
    # obj.merge(arr1, 0, arr2, 1)
    # print(arr1)