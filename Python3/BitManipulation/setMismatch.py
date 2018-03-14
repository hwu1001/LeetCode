# https://leetcode.com/problems/set-mismatch/description/

# Note that even though this problem is sort of similar to "Find the Duplicate Number"
# the strategies of binary search and the tortoise and the hare algorithms won't work
# in the same way since we have 1 to n integers with n elements. By not having n + 1
# elements the array requires further manipulation before those algorithms could be employed.break

# An example of why, say, binary search won't work immediately for something like:
# nums = [1,3,3,4,5]
# The mid-point 3 has 3 elements less than or equal to it, just like [1,2,3,4,5], so it becomes
# ambiguous which way to move our mid-point. If it was instead [1,2,3,4,5,3] there would be
# an indication that the duplicate is in the range 1 to mid-point since there are 4 elements less
# than or equal to 3.

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in range(1, len(nums) + 1):
            xor ^= i ^ nums[i - 1]
        differBit = xor & (~(xor - 1))
        missingOrDup = 0
        for i in range(1, len(nums) + 1):
            if i & differBit:
                missingOrDup ^= i
            if nums[i - 1] & differBit:
                missingOrDup ^= nums[i - 1]

        for num in nums:
            if num == missingOrDup:
                return [missingOrDup, missingOrDup ^ xor]
        return [missingOrDup ^ xor, missingOrDup]

    # Time: O(n)
    # Space: O(n)
    # Hash map solution
    def findErrorNums2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = {}
        missing = None
        dup = None
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for i in range(1, len(nums) + 1):
            if i in counter:
                if counter[i] > 1:
                    dup = i
            else:
                missing = i
            if missing is not None and dup is not None:
                break
        return [dup, missing]

    # Time: O(n)
    # Space: O(n)
    # Summation solution
    # This solution is generally not favored in compiled languages since it's prone
    # to overflow errors
    def findErrorNums3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        expectedSum = sum(range(1, len(nums) + 1))
        diff = expectedSum - sum(nums)
        diffWithNoDup = expectedSum - sum(set(nums))
        return [diffWithNoDup - diff, diffWithNoDup]

if __name__ == "__main__":
    # nums = [2,1,2,4]
    # nums = [1,2,3,3,5]
    # nums = [1,2,3,4,5,1,7]
    # nums = [1,2,6,4,5,6,7,8]
    nums = [1,2,3,4,5,6,7,8,9,10,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    # nums = [1,2,2,4,5,6]
    # nums = [1,2,3,4,5,6,8,8]
    obj = Solution()
    print(obj.findErrorNums(nums))