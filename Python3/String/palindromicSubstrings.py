# https://leetcode.com/problems/palindromic-substrings

class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(s, left, right):
            num_palindrome = 0
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                num_palindrome += 1
            return num_palindrome

        count = 0
        for i in range(len(s)):
            count += expandAroundCenter(s, i, i) # odd length string
            count += expandAroundCenter(s, i, i + 1) # even length string
        return count

if __name__ == "__main__":
    obj = Solution()
    assert(obj.countSubstrings("aaa") == 6)
    assert(obj.countSubstrings("abc") == 3)