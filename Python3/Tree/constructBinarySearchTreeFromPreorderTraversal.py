# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# This question confused me initially, here's the prompt:
# "Return the root node of a binary search tree that matches the given preorder traversal."
# It means "given the preorder traversal of a binary search tree"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from treeVisualizer import TreeNode, drawtree
from binaryTreePreorderTraversal import Solution as PreorderTraversal

class Solution:
    # Time: O(n)
    # Space: O(m) - max of m, where m is the number of nodes in the left-hand tree
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for cur_val in preorder[1:]:
            if cur_val < stack[-1].val:
                stack[-1].left = TreeNode(cur_val)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < cur_val:
                    last = stack.pop()
                last.right = TreeNode(cur_val)
                stack.append(last.right)
        return root

if __name__ == '__main__':
    obj = Solution()
    node = obj.bstFromPreorder([8,5,1,7,10,12])
    pre = PreorderTraversal()
    assert(pre.preorderTraversal(node) == [8,5,1,7,10,12])
