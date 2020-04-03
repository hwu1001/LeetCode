# https://leetcode.com/problems/daily-temperatures/

from typing import List
import heapq

class Solution:
    # Time: O(n) - Number of nodes in T
    # Space: O(w) - Where w is the number of allowed values in T
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                output[i] = stack[-1] - i
            stack.append(i)
        return output
    
    # First try at this, passed but very slow
    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        def _updateCache(pos: dict, temp: int, index: int):
            if temp not in pos:
                pos[temp] = [index]
                heapq.heapify(pos[temp])
            else:
                heapq.heappush(pos[temp], index)

        output = [0] * len(T)
        pos = {}
        temp_index = len(T) - 1
        largest_temp = 0
        while temp_index >= 0:
            temp = T[temp_index]
            if temp > largest_temp:
                largest_temp = temp
                _updateCache(pos, temp, temp_index)
                temp_index -= 1
                continue
            min_days = len(T)
            for val in range(temp + 1, 101):
                indices = pos[val] if val in pos else []
                for i in indices: # Because we sort indices we just loop through
                    if i > temp_index:
                        min_days = min(min_days, i - temp_index)
                        break
            if min_days != len(T):
                output[temp_index] = min_days 
            _updateCache(pos, temp, temp_index)
            temp_index -= 1
        return output

if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    obj = Solution()
    print(obj.dailyTemperatures(temps))