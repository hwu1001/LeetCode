# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from treeVisualizer import deserialize, TreeNode

class Solution:
    # Time: O(n) - Have to visit every node
    # Space: O(n) - Size of the call stack during the DFS
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0 
        def maxDepth(node: TreeNode) -> int:
            if node is None:
                return 0
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        maxDepth(root)
        return self.diameter

if __name__ == "__main__":
    root = deserialize('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]')
    obj = Solution()
    # root = deserialize('[1,2,3,4,5]')
    # root = deserialize('[]')
    print(obj.diameterOfBinaryTree(root))
