# https://leetcode.com/problems/remove-k-digits/

class Solution:
    # Greedy
    # Time: O(n)
    # Space: O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            # this is the greedy part, if a previous digit is larger than the next
            # one it will make the resulting number smaller
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0: # for cases like '111' or '1234'
            stack.pop()
            k -= 1
        non_zero_index = 0
        for digit in stack:
            if digit != '0':
                break
            non_zero_index += 1
        ans = ''.join(stack[non_zero_index:])
        return ans if ans != '' else '0'

if __name__ == '__main__':
    obj = Solution()
    assert(obj.removeKdigits('1432219', 3) == '1219')
    assert(obj.removeKdigits('10200', 1) == '200')
    assert(obj.removeKdigits('10', 2) == '0')
    assert(obj.removeKdigits('1234', 1) == '123')
    assert(obj.removeKdigits("1234567890", 9) == '0')