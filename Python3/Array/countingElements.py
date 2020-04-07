# 

from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = {}
        count = 0
        for num in arr:
            nums[num] = None
        for num in arr:
            if num + 1 in nums:
                count += 1
        return count

if __name__ == '__main__':
    # arr = [1,2,3] # 2
    # arr = [1,1,3,3,5,5,7,7] # 0
    # arr = [1,3,2,3,5,0] # 3
    arr = [1,1,2,2] # 2
    obj = Solution()
    print(obj.countElements(arr))