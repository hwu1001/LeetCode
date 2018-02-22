# https://leetcode.com/problems/rotate-array/description/

class Solution:
    # Time: O(n)
    # Space: O(n) - since we're taking list slices
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        numLen = len(nums)
        k = k % len(nums) # Mod just in case k is larger than len(nums)
        # Create a new list where we append the end of where the step is
        # to the front and the beginning to the back
        nums[:] = nums[numLen - k:] + nums[:numLen - k]
        return

    # Time: O(n)
    # Space: O(1)
    # Cyclic replacement solution
    def rotateCycle(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numLen = len(nums)
        k %= numLen
        count = 0
        start = 0
        # With these loops we start with index 0 and step k
        # So after completing an iteration over the entire list
        # We'll start again with index at 1 and step k again,
        # which will complete all shifts required
        while (count < numLen):
            cur = start
            prev = nums[start]
            while True:
                jumpIndex = (cur + k) % numLen
                # Since we overwrite the value we need to use next
                # save it off to use in the next iteration
                temp = nums[jumpIndex]
                nums[jumpIndex] = prev
                prev = temp
                cur = jumpIndex
                count += 1
                if start == cur:
                    break
            start += 1
    
    # Time: O(n) - n elements reversed 3 times
    # Space: O(1) - elements are reversed in place
    def rotateWithReverse(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        # Reverse the all elements
        reverse(nums, 0, len(nums) - 1)
        # Reverse the first k elements
        reverse(nums, 0, k - 1)
        # Reverse the last k elements
        reverse(nums, k, len(nums) - 1)
        return



if __name__ == "__main__":
    # vals = [1,2,3,4,5,6] # 2
    # vals = [1,2,3,4,5,6,7] # 3
    # vals = [1,2] # 2, 3
    vals = [-1, -100, 3, 99] # 3
    obj = Solution()
    obj.rotateWithReverse(vals, -1)
    print(vals)