# https://leetcode.com/problems/majority-element/description/

class Solution(object):
    # Time: O(nlog(n)) - For sorting
    # Space: O(1) - If we can alter the input, we can just use the current
    #               list, however if we should not then the space is O(n)
    # Sorting solution
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]
    
    # Time: O(n)
    # Space: O(1)
    # Boyer-Moore Voting Algorithm
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorElem = None
        count = 0
        for num in nums:
            if count == 0:
                majorElem = num
                count = 1
            elif num == majorElem:
                count += 1
            else:
                count -= 1
        return majorElem

if __name__ == "__main__":
    # l1 = [6,5,5]
    l1 = [3,2,2,3,2,5,2]
    sol = Solution()
    print(sol.majorityElement2(l1))