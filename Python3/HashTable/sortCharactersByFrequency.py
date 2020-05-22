# https://leetcode.com/problems/sort-characters-by-frequency/ 

from heapq import heappush, heappop

class Solution:
    # Heap sort
    # Time: O(nlogn)
    # Space: O(n)
    def frequencySort(self, s: str) -> str:
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        char_heap = []
        for c in char_map:
            heappush(char_heap, (-char_map[c], c))
        ans = []
        while char_heap:
            freq, char = heappop(char_heap)
            freq *= -1
            for _ in range(freq):
                ans.append(char)
        return ''.join(ans)

class Solution2:
    # Time: O(nlogn)
    # Space: O(n)
    def frequencySort(self, s: str) -> str:
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) - 1
        return ''.join(c * -c_freq for c, c_freq in sorted(char_map.items(), key=lambda x: x[1]))

class Solution3:
    # Bucket sort
    # Time: O(n)
    # Space: O(n)
    def frequencySort(self, s: str) -> str:
        ans = []
        bucket = [None for _ in range(len(s) + 1)]
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1

        for c, c_val in char_map.items():
            if bucket[c_val] is None:
                bucket[c_val] = []
            bucket[c_val].append(c)
        
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] is not None:
                for char in bucket[i]:
                    ans.append(char * i)
        return ''.join(ans)
        

if __name__ == '__main__':
    obj = Solution()
    assert(obj.frequencySort('tree') == 'eert')
    assert(obj.frequencySort('cccaaa') == 'aaaccc')
    assert(obj.frequencySort('Aabb') == 'bbAa')