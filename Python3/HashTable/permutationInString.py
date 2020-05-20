# https://leetcode.com/problems/permutation-in-string/

class Solution:
    # Sliding window
    # Time: O(n)
    # Space: O(1) - It's O(1) to store character occurrences because it's
    #               guaranteed to be lowercase a-z letters
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {chr(i): 0 for i in range(97, 123)}
        for c in s1:
            counter[c] += 1
        start = 0
        end = 0
        while end < len(s2):
            counter[s2[end]] -= 1
            while start <= end and counter[s2[end]] < 0:
                counter[s2[start]] += 1
                start += 1
            if end - start + 1 == len(s1):
                return True
            end += 1
        return False

if __name__ == '__main__':
    obj = Solution()
    assert(obj.checkInclusion('ab', 'eidbaooo') == True)
    assert(obj.checkInclusion('ab', 'eidboaoo') == False)