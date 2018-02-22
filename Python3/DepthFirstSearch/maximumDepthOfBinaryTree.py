# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from treeVisualizer import deserialize
from collections import deque

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree (holds the tree information on the call stack)
    # "Top-down" recursive solution
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _maxDepthHelper(node, depth):
            if node is None:
                return depth - 1
            if node.left is None and node.right is None:
                return depth
            return max(_maxDepthHelper(node.left, depth + 1), _maxDepthHelper(node.right, depth + 1))

        if not root:
            return 0
        return _maxDepthHelper(root, 1)
    
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree (holds the tree information on the call stack)
    # "Bottom-up" recursive solution
    def maxDepth2(self, root):
        if root is None:
            return 0
        leftDepth = self.maxDepth2(root.left)
        rightDepth = self.maxDepth2(root.right)
        return max(leftDepth, rightDepth) + 1
    
    # Time: O(n)
    # Space: O(h) - where h is the height of tree
    # Breath-first search iteration to count depth
    def maxDepth3(self, root):
        if root is None:
            return 0
        depth = 0
        nodeDeque = deque()
        nodeDeque.append(root)
        while nodeDeque:
            depth += 1
            for _ in range(len(nodeDeque)):
                node = nodeDeque.popleft()
                if node.left:
                    nodeDeque.append(node.left)
                if node.right:
                    nodeDeque.append(node.right)
        return depth
    
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Maybe more Pythonic iterative solution?
    def maxDepth4(self, root):
        if root is None:
            return 0
        depth = 0
        level = [root]
        while level:
            depth += 1
            level = [child for node in level for child in (node.left, node.right) if child]
        return depth
        
if __name__ == "__main__":
    root = deserialize('[3,9,20,null,null,15,7]')
    # root = deserialize('[37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]')
    # root = deserialize('[1,2,3,4,5]')
    # root = deserialize('[1,2,7,3,4,null,8,null,null,5,6,9]')
    # root = deserialize('[1]')
    obj = Solution()
    print(obj.maxDepth4(root))


            
