# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        close = {
            "]": "[", 
            "}": "{", 
            ")": "("
            }
        for char in s:
            if char in "({[":
                stack.append(char)
            # Check to see if stack is populated because a string of just
            # closing characters will result in an empty stack
            elif char in ")}]" and (not stack or close[char] != stack[-1]):
                return False
            else:
                stack.pop()
        # If our stack still has data in it, it means something wasn't closed
        # so it's invalid
        return stack == []

if __name__ == "__main__":
    s = "[]{}()"
    # s = "[{([{}])}]"
    # s = "}{"
    obj = Solution()
    print(obj.isValid(s))