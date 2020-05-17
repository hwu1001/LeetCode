# https://leetcode.com/problems/gas-station/

from typing import List

class Solution:
    # Time: O(n) - Need to visit all gas stations
    # Space: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        total = 0
        # This loop checks to see if a solution exists
        for i in range(len(gas)):
            total += gas[i] - cost[i]
        # If it costs more than gas available there
        # can't be a solution
        if total < 0:
            return -1
        tank = 0
        start = 0
        # This loop checks to see where the starting point is when there's
        # a solution
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # Because the problem said there's one unique solution
            # the first one found has to be the right one. Additionally
            # if starting at station A and going to station B cannot be done,
            # any station between A and B also cannot reach B
            if tank < 0:
                start = i + 1
                tank = 0
        return start

class Solution2:
    # Same as before in one loop
    # Time: O(n)
    # Space: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        tank = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1

if __name__ == '__main__':
    obj = Solution()
    assert(obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3)
    assert(obj.canCompleteCircuit([2,3,4], [3,4,3]) == -1)