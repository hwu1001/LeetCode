# https://leetcode.com/problems/valid-perfect-square/ 

class Solution:
    # Binary search
    # Time: O(logn)
    # Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <= high:
            mid = low + (high - low) // 2
            product = mid * mid
            if product == num:
                return True
            if product < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

class Solution2:
    # Newton's method
    # Time: O(logn)
    # Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        guess = num
        while guess * guess > num:
            guess = (guess + num/guess) // 2
        return guess * guess == num


if __name__ == '__main__':
    obj = Solution()
    tests = [1, 4, 9, 102, 12100, 66564, 448900, 998001, 2147483647]
    expected = [True, True, True, False, True, True, True, True, False]
    for i, v in enumerate(tests):
        assert(obj.isPerfectSquare(v) == expected[i])