# https://leetcode.com/problems/reverse-string-ii/description/

# The wording is a bit odd on this one, what it's saying is that
# for a given k, you'll take a slice of 2 times k characters in 
# your string s and reverse the first k characters of the slice.

class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverseCharList(chars):
            i = 0
            j = len(chars) - 1
            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
            return chars

        charList = list(s)
        for i in range(0, len(s), 2 * k):
            # Instead of writing our own function we could also
            # use the Python built-in, reversed()
            charList[i : i + k] = reverseCharList(charList[i : i + k])
        return "".join(charList)

if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    obj = Solution()
    print(obj.reverseStr(s,k))