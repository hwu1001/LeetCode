# https://leetcode.com/problems/word-break/description/

from collections import deque

class Solution(object):
    # Time: O(n^2)
    # Space: O(n)
    # Iterative solution scanning segments less than or equal to the
    # largest word in our wordDict and track found words in an array
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        # Optimize to only search segments that are as large as the largest
        # dictionary word
        longestWord = len(max(wordDict, key=len))
        found = [False] * (len(s) + 1)
        found[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, max(i - longestWord, 0) - 1, -1):
                if found[j] and s[j:i] in wordDict:
                    found[i] = True
                    break
        return found[len(s)]

    # Time: O(n^2)
    # Space: O(n)
    # Breath-first search where (I think) every index is a vertex and every edge
    # is a word from our wordDict
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        longestWord = len(max(wordDict, key=len))
        deq = deque([0])
        # Using the set to avoid repeating work where we know we've found a word match
        checkedIndices = set([0])
        while deq:
            curIndex = deq.popleft()
            for i in range(curIndex + 1, min(curIndex + longestWord, len(s)) + 1):
                if i in checkedIndices:
                    continue
                if s[curIndex:i] in wordDict:
                    if i == len(s):
                        return True
                    deq.append(i)
                    checkedIndices.add(i)
        return False

if __name__ == "__main__":
    # word = "aaaaaaa"
    # wordDict = ["aaaa","aaa"]
    # word = "cars"
    # wordDict = ["car","ca","rs"]
    word = "leetcode"
    wordDict = ["leet", "code"]
    obj = Solution()
    print(obj.wordBreak(word, wordDict))

