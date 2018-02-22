# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    # Time: O(n)
    # Space: O(1) - Note that it's constant since in this case 
    #               it will only be at maximum 26 key/value pairs
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLen = len(s)
        tLen = len(t)
        charCount = {}
        if tLen != sLen:
            return False
        for i in range(sLen):
            # https://docs.python.org/3/library/stdtypes.html#dict.get
            # The second parameter in the .get() method sets the default
            charCount[s[i]] = charCount.get(s[i], 0) + 1
            charCount[t[i]] = charCount.get(t[i], 0) - 1
        for char in charCount:
            if charCount[char] != 0:
                return False
        return True
    
    # Time: O(n)
    # Space: O(n)
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = s if len(s) > len(t) else t
        # if len(s) > len(t):
        #     l = s
        # else:
        #     l = t
        return all([t.count(char) == s.count(char) for char in set(l)])

if __name__ == "__main__":
    s = "roadr"
    r = "daror"
    obj = Solution()
    print(obj.isAnagram2(s, r))