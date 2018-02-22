# https://leetcode.com/problems/valid-palindrome/description/
from re import sub

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # In this version an empty string is considered valid:
        if not s:
            return True
        revIndex = -1
        sCopy = sub(r"[\W_]+", '', s).lower()
        for c in sCopy:
            if (c != sCopy[revIndex]):
                return False
            revIndex -= 1

        return True
    
    def isPalindrome2(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and s[start].isalnum():
                start += 1
            while start < end and s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
    # print(obj.isPalindrome("true eU rT"))
    # print(obj.isPalindrome("race a car"))