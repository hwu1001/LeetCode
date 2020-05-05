# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    # Time: O(n)
    # Space: O(1) - we could argue that the space has something like O(a)
    #               where a is the size of the alphabet, but since the alphabet
    #               is a fixed size I'm going to say constant size.
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        minIndex = len(s) - 1
        found = False
        chars = {}
        for i, c in enumerate(s):
            if c in chars:
                chars[c][0] = i
                chars[c][1] += 1
            else:
                chars[c] = [i, 1]
        for k in chars:
            if chars[k][1] == 1 and chars[k][0] <= minIndex:
                minIndex = chars[k][0]
                found = True
        if found:
            return minIndex
        else:
            return -1
    
    # Time: O(n)
    # Space: O(1) - we could argue that the space has something like O(a)
    #               where a is the size of the alphabet, but since the alphabet
    #               is a fixed size I'm going to say constant size
    # I don't prefer this answer because while it might run a bit faster for Python
    # I don't think it would be the preferred algorithm in compiled languages due to the
    # redundant work taking place with .count() and .index()
    def firstUniqChar2(self, s):
        if not s:
            return -1
        uniqs = []
        for c in set(s):
            if s.count(c) == 1:
                uniqs.append(s.index(c))
        if not uniqs:
            return -1
        else:
            return min(uniqs)

class Solution2:
    # Did this problem again for a challenge in May 2020, seemed simpler than the original answer I used
    # Time: O(n) - Two passes over string s
    # Space: O(1) - Only ever 26 characters plus a count, assuming a fixed integer for the number of characters
    def firstUniqChar(self, s: str) -> int:
        m  = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        for i, c in enumerate(s):
            if m[c] == 1:
                return i
        return -1

if __name__ == "__main__":
    obj = Solution()
    # test = obj.firstUniqChar2("loveleetcode")
    # test = obj.firstUniqChar2("leetcode")
    test = obj.firstUniqChar2("z")
    print(test)