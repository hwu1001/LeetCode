# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution:
    # Could use O(n + 1) space as an optimization, but I find the grid helpful for
    # understanding the full problem
    # Time: O(m * n) - Where m is the length of the first string and n is the length of the second
    # Space: O(m * n)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = ord(s1[i - 1]) + dp[i - 1][0]
        for j in range(1, n + 1):
            dp[0][j] = ord(s2[j - 1]) + dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j- 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    assert(obj.minimumDeleteSum("eat", "sea") == 231)
    assert(obj.minimumDeleteSum("delete", "leet") == 403)


# |     |               | s                | e             | a             |
# | --- | ------------- | ---------------- | ------------- | ------------- |
# |     | 0             | 115 (s)          | 216 (s, e)    | 313 (s, e, a) |
# | e   | 101 (e)       | 216 (s, e)       | 115 (s)       | 212 (s, a)    |
# | a   | 198 (e, a)    | 313 (s, e, a)    | 212 (s, a)    | 115 (s)       |
# | t   | 314 (e, a, t) | 429 (s, e, a, t) | 328 (s, a, t) | 231 (s, t)    |

# |     |                        | l                   | e                | e                | t                   |
# | --- | ---------------------- | ------------------- | ---------------- | ---------------- | ------------------- |
# |     | 0                      | 108 (l)             | 209 (l, e)       | 310 (l, e, e)    | 426 (l, e, e, t)    |
# | d   | 100 (d)                | 208 (l, d)          | 309 (l, e, d)    | 410 (l, e, e, d) | 526 (l, e, e, t, d) |
# | e   | 201 (d, e)             | 308 (l, d, e)       | 208 (l, d)       | 309 (l, e, d)    | 425 (l, e, t, d)    |
# | l   | 309 (d, e, l)          | 201 (d, e)          | 302 (e, d, e)    | 403 (e, e, d, e) | 519 (e, e, t, d, e) |
# | e   | 410 (d, e, l, e)       | 302 (d, e, e)       | 201 (d, e)       | 302 (e, d, e)    | 418 (e, t, d, e)    |
# | t   | 526 (d, e, l, e, t)    | 418 (d, e, e, t)    | 317 (d, e, t)    | 418 (e, d, e, t) | 302 (e, d, e)       |
# | e   | 627 (d, e, l, e, t, e) | 519 (d, e, e, t, e) | 418 (d, e, e, t) | 317 (d, e, t)    | 403 (e, d, e, e)    |