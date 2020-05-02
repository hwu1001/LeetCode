# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import List
from treeVisualizer import TreeNode, deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n + k) - where k is the number of unique values in the tree
    # Space: O(h + k) - where h is the height of the tree
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        mode_map = {}
        global_max = 0
        while stack:
            node = stack.pop()
            if node.val in mode_map:
                mode_map[node.val] += 1
            else:
                mode_map[node.val] = 1
            global_max = max(global_max, mode_map[node.val])

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return [val for val in mode_map if mode_map[val] == global_max]

class Solution2:
    # The real O(1) space solution is to use Morris traversal instead of using
    # a stack and do two passes with it
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    def findMode(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode, is_second_pass: bool):
            stack = []
            count = 0
            node = root
            prev = None
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                if prev is None or node.val == prev:
                    count += 1
                else:
                    if not is_second_pass:
                        self.tree_max = max(self.tree_max, count)
                    count = 1
                if is_second_pass and count == self.tree_max:
                    self.modes.append(node.val)
                prev = node.val
                node = node.right
            if not is_second_pass:
                self.tree_max = max(self.tree_max, count)

        if not root:
            return []
        self.modes = []
        self.tree_max = 0
        inorder(root, False) # first pass to get the mode
        inorder(root, True) # second pass to get values that have mode
        return self.modes


if __name__ == '__main__':
    obj = Solution()
    assert(sorted(obj.findMode(deserialize('[1,null,2,2]'))) == [2])
    assert(sorted(obj.findMode(deserialize('[3,1,5,1,2,5,6,1,null,null,null,5]'))) == [1,5])
    assert(sorted(obj.findMode(deserialize('[2,1,2]'))) == [2])
    assert(sorted(obj.findMode(deserialize('[1,null,2]'))) == [1,2])
    assert(sorted(obj.findMode(deserialize('[1,null,3,2,3]'))) == [3])
    assert(sorted(obj.findMode(deserialize('[6,2,8,0,4,7,9,null,null,2,6]'))) == [2,6])
