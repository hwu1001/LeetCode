# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from treeVisualizer import deserialize, TreeNode, drawtree
from collections import deque

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        q = deque()
        q.append([t1,t2])
        while q:
            cur = q.popleft()
            if cur[1] is None:
                continue
            cur[0].val += cur[1].val
            if cur[0].left is None:
                cur[0].left = cur[1].left
            else:
                q.append([cur[0].left, cur[1].left])
            if cur[0].right is None:
                cur[0].right = cur[1].right
            else:
                q.append([cur[0].right, cur[1].right])
        return t1
    
    # Time: O(n)
    # Space: O(h)
    def mergeTreesRecur(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTreesRecur(t1.left, t2.left)
            root.right = self.mergeTreesRecur(t1.right, t2.right)
            return root
        else:
            return t1 or t2

if __name__ == '__main__':
    t1 = deserialize('[1,3,2,5]')
    t2 = deserialize('[2,1,3,null,4,null,7]')
    obj = Solution()
    drawtree(obj.mergeTrees(t1, t2))