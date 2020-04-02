# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    # Wasn't sure on time/space - according to Leetcode it's
    # Space: O(4^n / sqrt(n))
    # Time: O(4^n / sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        def recurParen(leftRem: int, rightRem: int, parenList: List[str], index: int):
            if leftRem < 0 or rightRem < leftRem: # invalid state
                return
            if leftRem == 0 and rightRem == 0:
                allParen.append(''.join(parenList))
                return
            else:
                if leftRem > 0:
                    parenList[index] = '('
                    recurParen(leftRem - 1, rightRem, parenList, index + 1)
                if rightRem > leftRem:
                    parenList[index] = ')'
                    recurParen(leftRem, rightRem - 1, parenList, index + 1)
        allParen = []
        pList = [''] * (n * 2)
        recurParen(n, n, pList, 0)
        return allParen

if __name__ == "__main__":
    obj = Solution()
    l = obj.generateParenthesis(3)
    print(l)