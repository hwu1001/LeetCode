# https://leetcode.com/problems/merge-intervals/

from typing import List
from operator import itemgetter

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=itemgetter(0))
        merged = []
        i = 0
        while i < len(sorted_intervals):
            done = False
            start, end = sorted_intervals[i]
            while not done:
                if i >= len(sorted_intervals) - 1: # last item no need to compare
                    i += 1
                    merged.append([start, end])
                    break
                if end >= sorted_intervals[i + 1][0]:
                    start = min(start, sorted_intervals[i + 1][0])
                    end = max(end, sorted_intervals[i + 1][1])
                    i += 1
                else:
                    done = True
                    merged.append([start, end])
                    i += 1
        return merged

class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == '__main__':
    l = [[1,3],[15,18],[2,6],[8,10]]
    obj = Solution()
    assert(obj.merge(l) == [[1,6],[8,10],[15,18]])