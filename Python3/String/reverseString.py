# https://leetcode.com/problems/reverse-string/description/
class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i = 0
        j = len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)

    # Time: O(n)
    # Space: O(n)
    # More of a Python-specific solution
    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]