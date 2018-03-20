# https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    # My original solution - using a BFS
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        i = 0
        while i < len(nums) - 1:
            curNum = nums[i]
            maxNum = 0
            if i + curNum >= len(nums) - 1:
                count += 1
                break
            for j in range(i + 1, i + curNum + 1):
                if nums[j] >= maxNum:
                    maxNum = nums[j]
                    i = j
                else:
                    # Need to decrement if we don't have a new max
                    # since otherwise the solution will be closer to n^2
                    # E.g. (5,4,3,2,1,1,1) - Ideally jump to the second to last 1
                    # then jump to the finish
                    maxNum -= 1
            count += 1
            # Don't need below since we're allowed to assume the input always
            # makes it possible to jump to the end
            # if nums[i] == 0:
            #     break
        return count

    # Time: O(n)
    # Space: O(1)
    # Another BFS solution
    def jump2(self, nums):
        numLength = len(nums)
        steps = start = end = 0
        while end < numLength - 1:
            steps += 1
            maxEnd = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= numLength - 1:
                    return steps
                maxEnd = max(maxEnd, i + nums[i])
            start, end = end + 1, maxEnd
        return steps
                




if __name__ == "__main__":
    # nums = [4,3,2,0,1,1]
    # nums = [2,3,1,1,4]
    # nums = [4,2,0,0,1,1,4,4,4,0,4,0]
    nums = [5,4,3,2,1,1,1]
    # nums = [0]
    obj = Solution()
    print(obj.jump2(nums))