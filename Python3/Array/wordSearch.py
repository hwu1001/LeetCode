# https://leetcode.com/problems/word-search/

from typing import List
from collections import deque

class Solution:
    # Not 100% sure on this one
    # Time: O(m * n * l) - m is number of rows, n is number of columns, l is length of word
    # Space: O(l)
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0] and self.dfs(board, word, row, col):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, row: int, col: int):
        stack = []
        stack.append((row, col, 0, {}))
        while stack:
            r, c, word_index, visited = stack.pop()
            visited[(r, c)] = None
            if word_index >= len(word):
                continue
            if word_index == len(word) - 1 and board[r][c] == word[word_index]:
                return True
            if (r + 1 < len(board) and # down
                (r + 1, c) not in visited and
                board[r + 1][c] == word[word_index + 1]):
                    stack.append((r + 1, c, word_index + 1, visited.copy()))
            if (r - 1 >= 0 and # up
                (r - 1, c) not in visited and
                board[r - 1][c] == word[word_index + 1]):
                    stack.append((r - 1, c, word_index + 1, visited.copy()))
            if (c - 1 >= 0 and # left
                (r, c - 1) not in visited and
                board[r][c - 1] == word[word_index + 1]):
                    stack.append((r, c - 1, word_index + 1, visited.copy()))
            if (c + 1 < len(board[r]) and # right
                (r, c + 1) not in visited and
                board[r][c + 1] == word[word_index + 1]):
                    stack.append((r, c + 1, word_index + 1, visited.copy()))
        return False

# Alternate dfs
class Solution2:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

if __name__ == '__main__':
    board = [
        ['A','B','E','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    # word =  'SEE'
    # word = 'CEDFC'
    # word = 'SEED'
    # word = 'SEECEE'
    word = 'ABEESEEDASFC'

    # Should be true
    # board = [
    #     ["A","B","C","E"],
    #     ["S","F","E","S"],
    #     ["A","D","E","E"]
    # ]
    # word = "ABCESEEEFS"

    obj = Solution()
    print(obj.exist(board, word))