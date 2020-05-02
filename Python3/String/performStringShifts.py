# No problem listing - from monthly challenge

from typing import List
from collections import deque

class Solution:
    # Time: O(mn) - where m is the number of shifts and n is the length of the string
    # Space: O(n) - storing the string in an array
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if not s:
            return ''
        list_s = list(s)
        for sh in shift:
            index = 0
            temp = list_s[0]
            move = sh[1] if sh[0] == 1 else -sh[1]
            m = {}
            while len(m) != len(list_s):
                while index in m:
                    index += 1
                    temp = list_s[index]
                else:
                    m[index] = None
                nxt = (move + index) % len(list_s)
                temp, list_s[nxt] = list_s[nxt], temp
                index = nxt
        return ''.join(list_s)

class Solution2:
    # Time: O(mn) - where m is number of shifts to perform and n is the value of a given shift
    # Space: O(n) - Storing the string as a deque 
    def stringShift(self, s: str, shift: List[List[str]]) -> str:
        deq = deque(s)
        for sh in shift:
            if sh[0] == 0:
                for _ in range(sh[1]):
                    deq.append(deq.popleft())
            else:
                for _ in range(sh[1]):
                    deq.appendleft(deq.pop())
        return ''.join(deq)

if __name__ == '__main__':
    obj = Solution2()
    # The shifts are first element moving left (0) or right (1)
    # Second element is distance of shift
    # e.g. [0, 1] shift to the left one spaces or [1, 2] is shift right 2 spaces
    assert(obj.stringShift('abc', [[0,1],[1,2]]) == 'cab')
    assert(obj.stringShift('abcdefg', [[1,1],[1,1],[0,2],[1,3]]) == 'efgabcd')
    assert(obj.stringShift('yisxjwry', [[1,8],[1,4],[1,3],[1,6],[0,6],[1,4],[0,2],[0,1]]) == 'yisxjwry')