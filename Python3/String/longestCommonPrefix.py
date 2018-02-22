# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    # Time: O(S) - where S is the sum of all characters in all strings
    #              At worst we'll have n strings with equal length m to
    #              compare. Best case we have n * minLength, where minLength
    #              is the shortest string in the array
    # Space: O(1)
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # Use veritcal slices to check if all values are identical
        for i, strGroup in enumerate(zip(*strs)):
            if not self.checkAllIterableElemEqual(strGroup):
                return strs[0][:i]
        # We need to return min() because if we have two different words
        # that are all composed of the same letter, but different lengths
        # we could return the longer word
        return min(strs)


    def checkAllIterableElemEqual(self, iterable):
        return not iterable or all(iterable[0] == elem for elem in iterable)

if __name__ == "__main__":
    strs = [
        "testaa",
        "testa"
        "testb",
        "testc"
    ]
    obj = Solution()
    print(obj.longestCommonPrefix(strs))