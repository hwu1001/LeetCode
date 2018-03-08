# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from treeVisualizer import deserialize

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Iterative solution using visitation flags with a stack
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Not very elegant, but this is my original answer
        if not root:
            return []
        treeData = []
        visitedNode = False
        stack = []
        if root.right and not root.left:
            stack.append((root, False))
            stack.append((root, True))
        else:
            stack.append((root,True))
            stack.append((root, False))
        while stack:
            node, visitedNode = stack.pop()
            # Each node is appended twice below because in the pass where
            # we haven't visited the node we're exploring to see if there
            # are child nodes necessary to explore from it. And in the 
            # second pass we want to append the data from the node
            if node and not visitedNode:
                if node.left:
                    stack.append((node.left, True))
                    stack.append((node.left, False))
            elif node and visitedNode:
                if node.right:
                    stack.append((node.right, True))
                    stack.append((node.right, False))
                treeData.append(node.val)
        return treeData

    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Iterative solution with a stack
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeData = []
        stack = []
        node = root
        while(node or stack):
            while(node):
                stack.append(node)
                node = node.left
            node = stack.pop()
            treeData.append(node.val)
            node = node.right
        return treeData
    
    # Time: O(n)
    # Space: O(1)
    def inorderMorrisTraversal(self, root):
        curNode = root
        treeData = []
        while curNode:
            if curNode.left:
                node = curNode.left
                while node.right and node.right != curNode:
                    node = node.right
                if node.right is None:
                    # treeData.append(curNode.val) # Uncomment for preorder
                    node.right = curNode
                    curNode = curNode.left
                else:
                    treeData.append(curNode.val) # Move append here for inorder
                    node.right = None
                    curNode = curNode.right
            else:
                treeData.append(curNode.val)
                curNode = curNode.right
        return treeData

    # Time: O(n)
    # Space: O(h) - since the stack execution will hold the height
    #               of the tree in memory
    def inorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeData = []
        self._inorderTraversal(root, treeData)
        return treeData
    
    def _inorderTraversal(self, treeNode, treeData):
        if treeNode:
            self._inorderTraversal(treeNode.left, treeData)
            treeData.append(treeNode.val)
            self._inorderTraversal(treeNode.right, treeData)
            
if __name__ == "__main__":
    # root = deserialize('[1,null,2,3]')
    # root = deserialize('[1,2,3,4,5,null,6,null,null,7,8,9]')
    # root = deserialize('[1,2,2,null,3,null,3]')
    # root = deserialize('[1,2,2,3,4,4,3]')
    # root = deserialize('[1,2,2,3,null,null,3]')
    # root = deserialize('[1,2,2,3,4,4,3]')
    root = deserialize('[1,2,3,3,null,2,null]')
    obj = Solution()
    print(obj.inorderTraversal(root))
                