# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSum = 0
        expectedSum = 0
        i = 0
        # Just an explicit version of Gauss' formula
        for i, val in enumerate(nums):
            expectedSum += i
            numsSum += val
        # Since we're missing a number add the last value for what we would expect
        # so that we can subtract from it to get what's missing
        expectedSum += i + 1
        return expectedSum - numsSum

    def missingNumberXor(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missingNumberGauss(self, nums):
        numLen = len(nums)
        expectedSum = (numLen * (numLen + 1)) // 2
        return expectedSum - sum(nums)

if __name__ == "__main__":
    l = [9,6,4,2,3,5,7,0,1]
    # l = [3,0,1]
    # l = [5,3,2,0,1]
    obj = Solution()
    print(obj.missingNumberXor(l))

