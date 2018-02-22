# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from treeVisualizer import deserialize

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeData = []
        self._preorderTraversal(root, treeData)
        return treeData
    
    def _preorderTraversal(self, treeNode, treeData):
        if treeNode:
            treeData.append(treeNode.val)
            self._preorderTraversal(treeNode.left, treeData)
            self._preorderTraversal(treeNode.right, treeData)

    # Only append right nodes to the stack
    def preorderTraversal2(self, root):
        if not root:
            return []
        treeData = []
        rightNodes = []
        node = root
        while(node != None):
            treeData.append(node.val)
            if (node.right is not None):
                rightNodes.append(node.right)
            node = node.left
            if (node is None and rightNodes != []):
                node = rightNodes.pop()
        return treeData
    
    # Try to append all nodes to the stack
    def preorderTraversal3(self, root):
        treeData = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                treeData.append(node.val)
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
        return treeData
    
    def preorderMorrisTraversal(self, root):
        curNode = root
        treeData = []
        while curNode:
            if curNode.left:
                node = curNode.left
                # Need to check against curNode because node.right is set
                # to curNode temporarily to be able to traverse back up the tree
                while node.right and node.right != curNode:
                    node = node.right
                # If we get to the bottom of a node on the left side of the tree, repoint the right property
                # to the parent node if it's a left node. 
                # If it's a right node it will either point to the root or
                # to the parent of the right node's parent (the grandparent)
                if node.right is None:
                    treeData.append(curNode.val)
                    node.right = curNode
                    curNode = curNode.left
                # When we get to the bottom and we've been here before, reset the node
                # we changed previously so we could traverse upwards and make our current
                # node go right
                else:
                    node.right = None
                    curNode = curNode.right
            else:
                treeData.append(curNode.val)
                curNode = curNode.right
        return treeData


if __name__ == "__main__":
    # root = deserialize('[1,null,2,3,4]')
    # root = deserialize('[1,2,null,4,5,6,7]')
    root = deserialize('[1,2,null,null,7,8,9]')
    # root = deserialize('[1,2,3,4,5,6,7]')
    # root = deserialize("[37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]")

    obj = Solution()
    print(obj.preorderMorrisTraversal(root))
    