# https://leetcode.com/problems/longest-common-subsequence/

# Good explanation here: https://leetcode.com/problems/longest-common-subsequence/discuss/348884/C%2B%2B-with-picture-O(nm)

class Solution:
    # Solution could be optimized more by only using min(m, n) space since
    # we don't need the full grid to solve the problem
    # Time: O(mn)
    # Space: O(mn)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        grid = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 if (i - 1 < 0) or (j - 1 < 0) else (grid[i - 1][j - 1] + 1) 
                else:
                    top = 0 if (i - 1 < 0) else (grid[i - 1][j])
                    left = 0 if (j - 1 < 0) else (grid[i][j - 1])
                    grid[i][j] = max(top, left)
        return grid[m - 1][n - 1]

if __name__ == '__main__':
    obj = Solution()
    assert(obj.longestCommonSubsequence('abcdef', 'ace') == 3)
    assert(obj.longestCommonSubsequence('abc', 'abc') == 3)
    assert(obj.longestCommonSubsequence('abc', 'def') == 0)
    assert(obj.longestCommonSubsequence('pmjghexybyrgzczy', 'hafcdqbgncrcbihkd') == 4)
