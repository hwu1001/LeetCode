# https://leetcode.com/problems/shifting-letters/

from typing import List

class Solution:
    # Time: O(n) - where n is the number of shifts
    # Space: O(m) - storing the string in a list
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        letters = list(range(ord('a'),ord('z') + 1))
        ret = list(S)
        for i, sh in enumerate(shifts):
            if i > len(S) - 1:
                break
            index = ord(ret[i]) - ord('a')
            new_index = (sh + index) % 26
            ret[i] = chr(letters[new_index])
        return ''.join(ret)

class Solution2:
    # Time: O(n) - n is the length of the string
    # Space: O(n) - storing string in a list
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        ret = []
        shift = sum(shifts) % 26
        for i, char in enumerate(S):
            index = ord(char) - ord('a')
            ret.append(chr(ord('a') + (index + shift) % 26))
            shift = (shift - shifts[i]) % 26
        return ''.join(ret)


if __name__ == '__main__':
    obj = Solution()
    assert(obj.shiftingLetters('abc', [3,5,9]) == 'rpl')