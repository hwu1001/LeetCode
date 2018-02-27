# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # Time: O(n)
    # Space: O(w) - Only one level of the tree is ever stored at one time
    #               so the maximum storage is the widest part of the tree
    # Solution using breadth-first search with queue
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        nodeQueue = deque()
        nodeQueue.append(root)
        while nodeQueue:
            for _ in range(len(nodeQueue)):
                node = nodeQueue.popleft()
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
                node.left, node.right = node.right, node.left
        return root

    # Time: O(n)
    # Space: O(w) - where w is the tree at its widest level
    # Stack solution
    def invertTree2(self, root):
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root

    # Time: O(n)
    # Space: O(h)
    # Recursive solution using depth-first search
    def invertTreeRecur(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTreeRecur(root.right), self.invertTreeRecur(root.left)
        return root

if __name__ == "__main__":
    from treeVisualizer import deserialize
    root = deserialize('[4,2,7,1,3,6,9]')
    obj = Solution()
    root = obj.invertTreeRecur(root)
    level = [root]
    while level:
        print([node.val for node in level])
        level = [child for node in level for child in (node.left, node.right) if child]