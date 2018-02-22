# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from treeVisualizer import deserialize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Stack solution
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeData = []
        stack = []
        curNode = root
        lastNode = None
        while(curNode or stack):
            if curNode:
                stack.append(curNode)
                curNode = curNode.left
            else:
                topNode = stack[-1]
                if topNode.right and lastNode != topNode.right:
                    curNode = topNode.right
                else:
                    treeData.append(topNode.val)
                    lastNode = topNode
                    stack.pop()
        return treeData
    
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Stack solution using visitation flags
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        treeData = []
        stack = [(root, False)]
        node = root
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                treeData.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return treeData

    # Time: O(n)
    # Space: O(1)
    def postorderMorrisTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traceBack(fromNode, toNode):
            res = []
            curNode = fromNode
            while curNode is not toNode:
                res.append(curNode.val)
                curNode = curNode.right
            res.append(toNode.val)
            return res[::-1]

        dummyNode = TreeNode(0)
        dummyNode.left = root
        curNode = dummyNode
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
                    # treeData.append(curNode.val) # Move append here for inorder
                    treeData += traceBack(curNode.left, node)
                    node.right = None
                    curNode = curNode.right
            else:
                curNode = curNode.right
        return treeData

    # Time: O(n)
    # Space: O(h) - the stack execution will hold the height 
    #               of the tree in memory
    def postorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def _postorderTraversal(treeNode, treeData):
            if treeNode:
                _postorderTraversal(treeNode.left, treeData)
                _postorderTraversal(treeNode.right, treeData)
                treeData.append(treeNode.val)

        treeData = []
        _postorderTraversal(root, treeData)
        return treeData

if __name__ == "__main__":
    # root = deserialize('[1,null,2,3]')
    root = deserialize('[1,2,7,3,4,null,8,null,null,5,6,9]')
    obj = Solution()
    print(obj.postorderTraversal2(root))