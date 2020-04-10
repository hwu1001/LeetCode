
from typing import List
import collections

# Time: O(M + N) - where M and N are the lengths of S and T, respectively
# Space: O(M + N) - strings are immutable in Python so we have a new list for each string
class Solution:
    def processString(self, s: List[str]) -> List[str]:
        num_hashtags = 0
        index = len(s) - 1
        while index > -1:
            if s[index] == '#':
                num_hashtags += 1
            elif num_hashtags > 0:
                s[index] = '#'
                num_hashtags -= 1
            index -= 1
        return s

    def backspaceCompare(self, S: str, T: str) -> bool:
        S_arr = self.processString(list(S))
        T_arr = self.processString(list(T))
        s_index = 0
        t_index = 0
        while s_index < len(S_arr) and t_index < len(T_arr):
            while s_index < len(S_arr) - 1 and S_arr[s_index] == '#':
                s_index += 1
            while t_index < len(T_arr) - 1 and T_arr[t_index] == '#':
                t_index += 1
            
            if S_arr[s_index] != T_arr[t_index]:
                return False
            s_index += 1
            t_index += 1
        return True

# Time: O(M + N)
# Space: O(M + N)
class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.editorProcessor(S) == self.editorProcessor(T)
    def editorProcessor(self, string: str) -> str:
        res = collections.deque()
        l = 0
        for i in string:
            if i == "#":
                if  l > 0: 
                    res.pop()
                    l -= 1
            else:
                res.append(i)
                l += 1
        return ''.join(list(res))

# Time: O(M + N)
# Space: O(M + N)
class Solution3:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def finalStr(s: str):
            stack = []
            for char in s:
                if stack and char == '#':
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return finalStr(S) == finalStr(T)

if __name__ == '__main__':
    obj = Solution()
    assert(obj.backspaceCompare('ab#c', 'ad#c') == True)
    assert(obj.backspaceCompare('ab##', 'c#d#') == True)
    assert(obj.backspaceCompare('a##c', '#a#c') == True)
    assert(obj.backspaceCompare('a#c', 'b') == False)
