# https://leetcode.com/problems/ransom-note/

class Solution:
    # Time: O(m + n) - where m is the length of the ransom note and n is the number of letters in the magazine
    # Space: O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = {}
        for c in magazine:
            if c in magazine_chars:
                magazine_chars[c] += 1
            else:
                magazine_chars[c] = 1
        for c in ransomNote:
            if c not in magazine_chars:
                return False
            magazine_chars[c] -= 1
            if magazine_chars[c] < 0:
                return False
        return True

if __name__ == '__main__':
    obj = Solution()
    assert(obj.canConstruct('a', 'b') == False)
    assert(obj.canConstruct('aa', 'ab') == False)
    assert(obj.canConstruct('aa', 'aab') == True)