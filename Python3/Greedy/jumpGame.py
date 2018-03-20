# https://leetcode.com/problems/jump-game/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    # Original answer for my Greedy algorithm
    # using something like a BFS search
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(nums) - 1:
            curNum = nums[i]
            maxNum = 0
            if i + curNum >= len(nums) - 1:
                i += curNum
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
            if nums[i] == 0:
                break
        return i >= len(nums) - 1
    

    # Time: O(n)
    # Space: O(1)
    def canJump2(self, nums):
        reachable = 0
        for i in range(len(nums)):
            if i > reachable: 
                return False
            reachable = max(reachable, i + nums[i])
        return True
    
    # Time: O(n)
    # Space: O(1)
    # Bottom-up Greedy algorithm
    def canJump3(self, nums):
        lastPos=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=lastPos:
                lastPos=i
        return lastPos==0

if __name__ == "__main__":
    # nums = [2,3,1,1,4] # true
    nums = [3,2,1,0,4] # False
    # nums = [4,1,1,1,1,0] # True
    # nums = [2,5,0,0] # true
    # nums = [4,2,0,0,1,1,4,4,4,0,4,0] # True
    # nums = [2,3,0,0,0,1,0]
    # nums = [5,4,3,2,1]
    obj = Solution()
    print(obj.canJump2(nums))
            