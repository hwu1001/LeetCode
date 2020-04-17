

class Solution:
    # Time: O(n) - At most 2 passes over the length of the string
    # Space: O(n) - Stores at most the full string
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        left_stack = []
        star_stack = []
        for i, char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else: # )
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        for _ in range(len(left_stack)):
            if star_stack and left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
        return left_stack == []

class Solution2:
    # Greedy algorithm that keeps track of the "balance" of the string
    # Time: O(n)
    # Space: O(n)
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if (hi < 0):
                break
            lo = max(lo, 0)
        return lo == 0

if __name__ == '__main__':
    obj = Solution()
    assert(obj.checkValidString('()') == True)
    assert(obj.checkValidString('(*)') == True)
    assert(obj.checkValidString('(*))') == True)
    assert(obj.checkValidString('((**)') == True)
    assert(obj.checkValidString('(()') == False)
    assert(obj.checkValidString('(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)') == True)
