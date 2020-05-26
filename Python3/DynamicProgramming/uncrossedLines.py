# https://leetcode.com/problems/uncrossed-lines/

from typing import List

class Solution:
    # Same as longest common subsequence
    # Time: O(m * n) - where m is the length of list A and n is length of list B
    # Space: O(m * n)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

if __name__ == '__main__':
    obj = Solution()
    assert(obj.maxUncrossedLines([1,4,2], [1,2,4]) == 2)
    assert(obj.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]) == 2)
    assert(obj.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]) == 3)

#   1 4 2
# 1 1 1 1
# 2 1 1 2
# 4 1 2 2

#   1 3 7 1 7 5
# 1 1 1 1 1 1 1
# 9 1 1 1 1 1 1
# 2 1 1 1 1 1 1
# 5 1 1 1 1 1 2
# 1 1 1 1 2 2 2

#    2 5 1 2 5
# 10 0 0 0 0 0
# 5  0 1 1 1 1
# 2  1 1 1 1 1
# 1  1 1 2 2 2
# 5  1 2 2 2 3
# 2  1 2 2 3 3