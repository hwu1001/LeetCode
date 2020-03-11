# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from treeVisualizer import deserialize, TreeNode, drawtree

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
            if stack:
                node.right = stack[-1]
                node.left = None
        return
    
    # Time: O(nlog(n)) - ?
    # Space: O(1)
    def flatten2(self, root: TreeNode) -> None:
        now = root
        while now:
            if now.left:
                # Find current node's prenode that links to current node's right subtree
                pre = now.left
                while pre.right:
                    pre = pre.right
                pre.right = now.right
                # Use current node's left subtree to replace its right subtree (original right)
                # sub is already linked by current node's prenode
                now.right = now.left
                now.left = None
            now = now.right

if __name__ == '__main__':
    root = deserialize('[1,2,5,3,4,null,6]')
    obj = Solution()
    obj.flatten2(root)
    drawtree(root)
    
