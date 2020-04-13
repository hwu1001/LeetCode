# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq

class Solution:
    # Time: O(nlogn) - Sort and iterate over list
    # Space: O(n) - Storing the entire last in heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        hq = []
        heapq.heapify(hq)
        for stone in stones:
            heapq.heappush(hq, (-stone, stone))
        while len(hq) > 1:
            last = heapq.heappop(hq)
            second_last = heapq.heappop(hq)
            diff = last[1] - second_last[1]
            if diff != 0:
                heapq.heappush(hq, (-diff, diff))
        return 0 if len(hq) == 0 else heapq.heappop(hq)[1]

if __name__ == '__main__':
    l = [2,7,4,1,8,1]
    obj = Solution()
    assert(obj.lastStoneWeight(l) == 1)