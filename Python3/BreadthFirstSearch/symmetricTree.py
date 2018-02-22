# https://leetcode.com/problems/symmetric-tree/description/

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
    # Space: O(h) - where h is the height of the tree
    # Iterative solution using breadth-first search with deque
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isLevelSymmetric(level):
            # Really we're checking to see if the level is a palindrome
            revIndex = -1
            for i in range(len(level) // 2):
                if level[i] is None and level[revIndex] is None:
                    revIndex -= 1
                    continue
                if level[i] is None or level[revIndex] is None or level[i].val != level[revIndex].val:
                    return False
                revIndex -= 1
            return True
            
        if not root:
            return True
        nodeDeque = deque()
        nodeDeque.append(root)
        # https://docs.python.org/3/library/functions.html#any
        while any(nodeDeque):
            for _ in range(len(nodeDeque)):
                node = nodeDeque.popleft()
                # Note that level includes null nodes, since those will be needed to compare
                # for symmetry in the level
                if not node:
                    nodeDeque.append(node)
                    continue
                nodeDeque.append(node.left)
                nodeDeque.append(node.right)
            if not isLevelSymmetric(nodeDeque):
                return False
        return True

    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Iterative solution using a stack (could use a queue instead though)
    def isSymmetric2(self, root):
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()

            if right is None and left is None:
                continue
            
            if right is None or left is None or right.val != left.val:
                return False
            # Inner branches
            stack.append(right.left)
            stack.append(left.right)
            # Outer branches
            stack.append(right.right)
            stack.append(left.left)
        return True
    
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree stored on the stack execution
    # Recursive solution
    def isSymmetric3(self, root):
        def _isSymmetricHelper(leftNode, rightNode):
            if leftNode is None and rightNode is None:
                return True
            if leftNode is None or rightNode is None or leftNode.val != rightNode.val:
                return False
            return _isSymmetricHelper(leftNode.left, rightNode.right) and _isSymmetricHelper(leftNode.right, rightNode.left)

        if not root:
            return True
        return _isSymmetricHelper(root.left, root.right)


if __name__ == "__main__":
    # root = deserialize('[1]')
    # root = deserialize('[1,2,2,null,3,null,3]') # False
    # root = deserialize('[1,2,2,3,4,4,3]') # True
    # root = deserialize('[1,2,2,3,4,5,3]') # False
    # root = deserialize('[1,2,2,3,null,null,3]') # True
    root = deserialize('[1,2,2,null,3,3]') # True
    # root = deserialize('[1,2,3,3,null,2,null]') # This case shows why you can't use inorder traversal in this problem - should return False
    obj = Solution()
    print(obj.isSymmetric2(root))