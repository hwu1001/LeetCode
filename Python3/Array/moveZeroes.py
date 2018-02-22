# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    # This is the optimal solution since it requires the least amount of read/writes
    # We're only swapping data once we have a match, rather than at every element
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
        return
    
    # Time: O(n)
    # Space: O(1)
    # This was my first iteration on the problem, before realizing you don't need
    # to delete values and then re-add them at the end
    def moveZeroesDel(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        count = 0
        i = 0
        while (i < len(nums)):
            if i < 0:
                i = 0
            if nums and nums[i] == 0:
                del nums[i]
                count += 1
                i -= 1
            else:
                i += 1
        nums[i:] = [0] * count
        return

    # Time: O(n)
    # Space: O(1)
    # Similar to the solution deletion, except you just overwrite the values instead
    # The count of zeroes is kept and then added at the end
    def moveZeroesIterate(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        index = 0
        for i, num in enumerate(nums):
            # For each non-zero increment our count and set the value
            # in the array for it at the front of the list
            if num != 0:
                nums[index] = nums[i]
                index += 1
        # Iterate from the beginning of where the non-zero numbers are
        # through the end of the list and append zeroes
        for j in range(index, len(nums)):
            nums[j] = 0


if __name__ == "__main__":
    test = [0, 1, 0, 3, 12]
    # test = [0, 0, 1]
    # test = [0]
    # test = [0, 0, 0]
    obj = Solution()
    obj.moveZeroes(test)
    print(test)