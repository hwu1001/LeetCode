# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

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
    # Space: O(n)
    # Solution using a deque
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        treeData = []
        index = 0
        nodeDeque = deque()
        nodeDeque.append(root)
        while nodeDeque:
            # level = []
            treeData.append([])
            count = len(nodeDeque)
            for _ in range(count):
                node = nodeDeque.popleft()
                # level.append(node.val)
                treeData[index].append(node.val)
                if node.left:
                    nodeDeque.append(node.left)
                if node.right:
                    nodeDeque.append(node.right)
            # treeData.append(level)
            index += 1
        return treeData
    
    # Time: O(n)
    # Space: O(n)
    # Solution using list comprehension
    def levelOrder2(self, root):
        if not root:
            return []
        treeData = []
        level = [root]
        while level:
            treeData.append([node.val for node in level])
            # Create new level to append data from in the next iteration
            # Do not append null nodes
            level = [child for node in level for child in (node.left, node.right) if child]
        return treeData

    # Time: O(n)
    # Space: O(n)
    def levelOrderRecursion(self, root):
        def _levelOrderHelper(node, treeData, height):
            if node is None:
                return
            if height >= len(treeData):
                treeData.append([])
            treeData[height].append(node.val)
            _levelOrderHelper(node.left, treeData, height + 1)
            _levelOrderHelper(node.right, treeData, height + 1)

        treeData = []
        _levelOrderHelper(root, treeData, 0)
        return treeData




if __name__ == "__main__":
    root = deserialize('[1,2,7,3,4,null,8,null,null,5,6,9]') # [[1], [2, 7], [3, 4, 8], [5, 6, 9]]
    # root = deserialize('[37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]') # [[37], [-34, -48], [-100, -100, 48], [-54], [-71, -22], [8]]
    # root = deserialize('[3,9,20,null,null,15,7]') # [[3], [9, 20], [15, 7]]
    # root = deserialize('[1,2,null,3,4]') # [[1], [2], [3, 4]]
    # root = deserialize('[1,null,2,3,null,4,5]') # [[1], [2], [3], [4, 5]]
    # root = deserialize('[1,2,3,4,5]') # [[1], [2, 3], [4, 5]]
    # root = deserialize('[1,2,3,4,5,null,null,null,null,6,7]') # [[1], [2, 3], [4, 5], [6, 7]]
    # root = deserialize('[1,2,3,4,null,null,5]') # [[1], [2, 3], [4, 5]]
    # root = deserialize('[3,9,20,null,7,null,null,8,9]') # [3], [9, 20], [7], [8, 9]]
    obj = Solution()
    print(obj.levelOrder(root))

