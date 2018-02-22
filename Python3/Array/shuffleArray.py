# https://leetcode.com/problems/shuffle-an-array/description/

from random import randrange

# Time: O(n)
# Space: O(n)
class Solution:
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.reset()
    # param_2 = obj.shuffle()

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.shuffleNums = nums[:]
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.shuffleNums = self.nums[:]
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        numSize = len(self.shuffleNums)
        # Use Fisher-Yates algorithm for shuffling (you could also use random.shuffle() but sort of
        # defeats the purpose of the exercise)
        # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        for i in range(numSize):
            # No need to seed since random methods are seeded when you import random module
            randNum = randrange(0, numSize)
            self.shuffleNums[i], self.shuffleNums[randNum] = self.shuffleNums[randNum], self.shuffleNums[i]
        return self.shuffleNums

if __name__ == "__main__":
    nums = list(range(1, 26))
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    assert param_1 == nums
    print(param_1)
    print(param_2)
        


