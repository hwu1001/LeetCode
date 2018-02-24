# https://leetcode.com/problems/3sum/description/

class Solution:
    # Time: O(n^2)
    # Space: O(n^2) - Once for the return values, once for the tried values
    #                 to avoid running threeSum twice on the same number.
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Find every two sum in nums for a given target
        def twoSum(nums, target):
            ret = []
            numsDict = {}
            for i, val in enumerate(nums):
                temp = target - val
                if temp in numsDict:
                    ret.append([numsDict[temp], i])
                else:
                    numsDict[val] = i
            return ret

        res = {}
        triedNums = {}
        for i, num in enumerate(nums):
            if num in triedNums:
                continue
            else:
                triedNums[num] = 1
            temp = twoSum(nums[i + 1:len(nums)], 0 - num)
            if temp:
                temp = [[nums[val + i + 1] for val in l] for l in temp]
                for l in temp:
                    l.append(num)
                    l.sort()
                tup = [tuple(l) for l in temp]
                for t in tup:
                    if t not in res:
                        res[t] = 1
        return [list(tup) for tup in res.keys()]
    
    # Time: O(n^2)
    # Space: O(n) - Not counting the space used in the sorting of
    #               our input. Worst case sorting for that would be O(n)
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Could also do var = sorted(nums) if we didn't want to alter
        # nums in place
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # Since we sorted nums if there's a number greater than 0
            # we know there cannot be a sum of 0 since it will just be
            # sums of positive numbers
            if nums[i] > 0:
                break
            # If we're at the first try or if we're at a number
            # that is not equal to a number we've already tried
            # then run two sum on it
            if (i == 0 or (i > 0 and nums[i] != nums[i - 1])):
                low = i + 1
                high = len(nums) - 1
                targetSum = 0 - nums[i] # Target is 0
                while (low < high):
                    if (nums[low] + nums[high] == targetSum):
                        res.append([nums[i], nums[low], nums[high]])
                        # Move past duplicate numbers on both ends
                        while (low < high and nums[low] == nums[low + 1]):
                            low += 1
                        while (low < high and nums[high] == nums[high - 1]):
                            high -=1
                        low += 1
                        high -= 1
                    elif (nums[low] + nums[high] < targetSum):
                        while (low < high and nums[low] == nums[low+1]):
                            low +=1
                        low += 1
                    else:
                        while (low < high and nums[high] == nums[high - 1]):
                            high -= 1
                        high -= 1
        return res

if __name__ == "__main__":
    # l = [-1, 0, 1, 3, -2, -4]
    l = [-2,0,1,1,2]
    # print(len(l))
    obj = Solution()
    print(obj.threeSum2(l))