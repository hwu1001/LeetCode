# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    # Time: O(n) - Where n is the length of the string s
    # Space: O(min(m, n)) - Where m is the character set
    # Optimized sliding window approach
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest_len = 0
        start_pos = 0
        char_set = {}
        for cur_ndx, char in enumerate(s):
            if char in char_set:
                next_pos = char_set[char] + 1
                if next_pos > start_pos:
                    start_pos = next_pos
            char_set[char] = cur_ndx
            str_len = cur_ndx - start_pos + 1 # Add one to account for string length
            if str_len > longest_len:
                longest_len = str_len
        return longest_len

if __name__ == "__main__":
    obj = Solution()
    assert(obj.lengthOfLongestSubstring("abcabcbb") == 3)
    assert(obj.lengthOfLongestSubstring("bbbbb") == 1)
    assert(obj.lengthOfLongestSubstring("pwwkew") == 3)
    assert(obj.lengthOfLongestSubstring("abcbad") == 4)
