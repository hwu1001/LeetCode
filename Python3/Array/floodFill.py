# https://leetcode.com/problems/flood-fill/ 

from typing import List

class Solution:
    # Time: O(n)
    # Space: O(n)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def isInBounds(row: int, col: int) -> bool:
            return row >= 0 and row < len(image) and col >= 0 and col < len(image[row])
        cur_color = image[sr][sc]
        if cur_color == newColor: # this check is very important
            return image
        image[sr][sc] = newColor
        stack = [(sr, sc)]
        while stack:
            row, col = stack.pop()
            # up, down, left, right
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if isInBounds(r, c) and image[r][c] == cur_color:
                    image[r][c] = newColor
                    stack.append((r, c))
        return image

class Solution2:
    # Time: O(n)
    # Space: O(n)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_len = len(image)
        col_len = len(image[0])
        cur_color = image[sr][sc]
        if cur_color == newColor:
            return image
        def dfs(row: int, col: int) -> None:
            if image[row][col] == cur_color:
                image[row][col] = newColor
                if row >= 1:
                    dfs(row - 1, col)
                if row + 1 < row_len:
                    dfs(row + 1, col)
                if col >= 1:
                    dfs(row, col - 1)
                if col + 1 < col_len:
                    dfs(row, col + 1)
        dfs(sr, sc)
        return image


if __name__ == '__main__':
    obj = Solution()
    image = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
        ]
    new_image = [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1]
        ]
    assert(obj.floodFill(image, 1, 1, 2) == new_image)