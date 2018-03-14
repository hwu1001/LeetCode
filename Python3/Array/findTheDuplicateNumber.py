# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    # Time: O(n)
    # Space: O(1)
    # Solution using cycle detection - Floyd's tortoise and hare
    # https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
    # http://keithschwarz.com/interesting/code/find-duplicate/FindDuplicate.python.html
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        tortoise = nums[0]
        hare = nums[nums[0]]
        # Keep iterating pointers until they meet inside the cycle
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
        # Since tortoise will be inside the cycle, reset hare and 
        # iterate forward until hare meets tortoise inside the cycle
        hare = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise
    
    # Time: O(nlog(n))
    # Space: O(1)
    # Binary search solution
    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            # The sum will be the number of elements in the range 1 to mid
            # If this sum is <= mid then there are n + 1 - sum elements in the range
            # mid + 1 to n. So there are at least n + 1 - mid elements in a range of size
            # n - mid. Thus this range must contain a duplicate.
            if sum(i <= mid for i in nums) <= mid:
                low = mid + 1
            # If the sum > mid then there are more mid elements in the range 1 to mid
            # and thus this range contains a duplicate
            else:
                high = mid
        return low

    # Time: O(n)
    # Space: O(n)
    # Set solution
    def findDuplicate3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        return -1

    # Time: O(n)
    # Space: O(1) or O(n) - depending on if we can alter the original array
    #                       in this particular LeetCode problem you're not supposed to 
    #                       alter the original array,
    # Sorting solution
    def findDuplicate4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

if __name__ == "__main__":
    # nums = [1,3,3,3,3,6,7,3]
    # nums = [1,1]
    nums = [1,5,2,3,4,6,7,1]
    obj = Solution()
    print(obj.findDuplicate(nums))

