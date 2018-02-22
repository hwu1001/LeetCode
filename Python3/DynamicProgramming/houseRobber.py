# https://leetcode.com/problems/house-robber/description/
class Solution:
    # Time: O(n)
    # Space: O(1)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ifRobbedPrev = 0
        ifDidntRobPrev = 0
        # We go through all the values, we maintain two counts, 1) if we rob this house, 2) if we didn't rob this house
        for house in nums:
            # If we rob current house, previous house shouldn't be robbed. So, add the current value to previous one.
            curRobbed = ifDidntRobPrev + house
            # If we don't rob current house, then the count should be max of the previous house robbed and not robbed
            curNotRobbed = max(ifDidntRobPrev, ifRobbedPrev)

            # Update values for the next round
            ifDidntRobPrev = curNotRobbed
            ifRobbedPrev = curRobbed
            # ifRobbedPrev, ifDidntRobPrev = ifDidntRobPrev, max(ifDidntRobPrev + house, ifRobbedPrev)
        return max(ifRobbedPrev, ifDidntRobPrev)

    # Time: O(n)
    # Space: O(1)
    def rob2(self, nums):
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
            # The above statement is equivalent to the following:
            # temp = now
            # now = max(last + i, now)
            # last = temp
        return now

if __name__ == "__main__":
    # houses = [1,0,1,9,6] # 10
    # houses = [2,1,1,2] # 4
    # houses = [6,1,0,1,7] # 13
    # houses = [4,3,1,4] # 8
    # houses = [4,3,1,4,10]
    # houses = [6,0,0,2,0,0,0,5] # 13
    houses = [12,21,6,15,2,0,50]
    obj = Solution()
    print(obj.rob2(houses))
