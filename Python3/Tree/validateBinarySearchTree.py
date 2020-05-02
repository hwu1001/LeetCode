# https://leetcode.com/problems/validate-binary-search-tree/

from treeVisualizer import deserialize, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower_bound, upper_bound = stack.pop()
            if node.val <= lower_bound or node.val >= upper_bound:
                return False
            if node.right:
                stack.append((node.right, node.val, upper_bound))
            if node.left:
                stack.append((node.left, lower_bound, node.val))
        return True

if __name__ == '__main__':
    obj = Solution()
    assert(obj.isValidBST(deserialize('[2,1,3]')) == True)
    assert(obj.isValidBST(deserialize('[3,1,5,0,2,4,6]')) == True)
    assert(obj.isValidBST(deserialize('[5,1,4,null,null,3,6]')) == False)
    assert(obj.isValidBST(deserialize('[1,0,1]')) == False)
    assert(obj.isValidBST(deserialize('[10,5,15,null,null,6,20]')) == False)