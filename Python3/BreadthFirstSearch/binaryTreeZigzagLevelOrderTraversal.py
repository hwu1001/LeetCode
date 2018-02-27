# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    # Time: O(n)
    # Space: O(n)
    # Solution using list comprehension
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        zigzag = []
        level = [root]
        startLeft = False
        while level:
            zigzag.append([node.val for node in level])
            # Note that we iterate over the reverse of the level to get the zigzag result
            if startLeft:
                level = [child for node in level[::-1] for child in (node.left, node.right) if child]
                startLeft = False
            else:
                level = [child for node in level[::-1] for child in (node.right, node.left) if child]
                startLeft = True
        return zigzag

    # Time: O(n)
    # Space: O(n)
    # Solution using queue
    def zigzagLevelOrder2(self, root):
        if not root:
            return []
        zigzag = []
        nodeQueue = deque()
        nodeQueue.append(root)
        index = 0 # Use index as flag for zigzag
        while nodeQueue:
            zigzag.append([])
            for _ in range(len(nodeQueue)):
                node = nodeQueue.popleft()
                zigzag[index].append(node.val)
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            if index % 2 != 0:
                zigzag[index].reverse()
            index += 1
        return zigzag


if __name__ == "__main__":
    from treeVisualizer import deserialize
    root = deserialize('[3,9,20,null,null,15,7]')
    obj = Solution()
    print(obj.zigzagLevelOrder(root))
