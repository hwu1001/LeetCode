# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree on the execution stack
    # Recursive solution
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def pathSumHelper(node, count, sum):
            if not node:
                return False
            if not node.right and not node.left:
                return node.val + count == sum
            
            return pathSumHelper(node.left, node.val + count, sum) or pathSumHelper(node.right, node.val + count, sum)
            
        count = 0
        return pathSumHelper(root, count, sum)
    
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Post-order traversal solution
    def hasPathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        treeSum = 0
        stack = [(root, False)]
        node = root
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                treeSum -= node.val
            else:
                treeSum += node.val
                if not node.left and not node.right and treeSum == sum:
                    return True
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return False
    
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree
    # Similar to post-order traversal, but instead of revisitng nodes,
    # it stores the difference of the target and the node's value in order
    # to search for the desired path sum at the leaf nodes
    def hasPathSum3(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        stack = [(root, sum)]
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right and node.val == val:
                    return True
                stack.append((node.right, val - node.val))
                stack.append((node.left, val - node.val))
        return False

if __name__ == "__main__":
    from treeVisualizer import deserialize
    root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]') # 22 - true
    # root = deserialize('[1,-2,-3,1,3,-2,null,-1]') # 3 - false
    # root = deserialize('[2,-1,null,null,-5,7,0,null,-5,null,-1,null,-4,-5]') # -10 - true
    obj = Solution()
    print(obj.hasPathSum3(root, 22))