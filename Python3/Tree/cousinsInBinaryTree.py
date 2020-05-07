# https://leetcode.com/problems/cousins-in-binary-tree/

from treeVisualizer import deserialize, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS saving the depth and parents of nodes x and y
    # Time: O(n)
    # Space: O(h) - The height of the tree kept in the stack
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        stack = [(root, 0, None)]
        vals = {}
        while stack and (x not in vals or y not in vals):
            node, depth, parent = stack.pop()
            if node.val == x or node.val == y:
                vals[node.val] = (depth, parent)
            if node.right:
                stack.append((node.right, depth + 1, node))
            if node.left:
                stack.append((node.left, depth + 1, node))
        if x not in vals or y not in vals:
            return False
        x_depth, x_parent = vals[x]
        y_depth, y_parent = vals[y]
        return x_depth == y_depth and x_parent != y_parent

if __name__ == '__main__':
    obj = Solution()
    assert(obj.isCousins(deserialize('[1,2,3,4]'), 4, 3) == False)
    assert(obj.isCousins(deserialize('[1,2,3,null,4,null,5]'), 5, 4) == True)
    assert(obj.isCousins(deserialize('[1,2,3,null,4]'), 2, 3) == False)