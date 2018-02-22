# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Found this one a bit odd to start, but I think it's more targeted towards compiled
# languages that have to say how long their arrays are at compile time

class Solution:
    # Time: O(n)
    # Space: O(1)
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numLen = len(nums)
        if numLen == 0:
            return 0
        i = 0
        for j in range(1, numLen):
            # Iterate through list and move unique values
            # to the front of the list, where we keep i as our
            # index to the most recent unique value
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        # Return length of list
        return i + 1

if __name__ == "__main__":
    # nums = [1,1,2,3,3,3,3,4,4,4,4,5]
    # nums = [1,2,3]
    nums = [0]
    obj = Solution()
    newLen = obj.removeDuplicates(nums)
    print(nums[:newLen])
            
