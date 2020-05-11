# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List

class Solution:
    # Sliding window
    # See post for more explanation:
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem
    # Time: O(n)
    # Space: O(n) - It's O(1) to store character occurrences because it's
    #               guaranteed to be lowercase a-z letters, but have to store
    #               result too
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = {}
        for char in p:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1
        start = 0
        end = 0
        counter = len(m)
        matches = []
        while end < len(s):
            end_c = s[end]
            if end_c in m:
                m[end_c] -= 1
                if m[end_c] == 0:
                    counter -= 1
            end +=1
            while counter == 0:
                start_c = s[start]
                if start_c in m:
                    if m[start_c] == 0:
                        counter += 1
                    m[start_c] += 1
                if end - start == len(p):
                    matches.append(start)
                start += 1
        return matches

class Solution2:
    # Another sliding window implementation
    # Time: O(n)
    # Space: O(n)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        matches = []
        counter = {chr(c): 0 for c in range(97, 123)}
        for c in p:
            counter[c] += 1
        start = 0
        end = 0
        while end < len(s):
            counter[s[end]] -= 1
            while start <= end and counter[s[end]] < 0:
                counter[s[start]] += 1
                start += 1
            if end - start + 1 == len(p):
                matches.append(start)
            end += 1
        return matches



if __name__ == '__main__':
    obj = Solution()
    assert(obj.findAnagrams('cbaebabacd', 'abc') == [0, 6])