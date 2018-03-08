# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Time: O(n)
    # Space: O(h) - where h is the height of the tree, 
    #               stored in the stack execution
    # Recursive solution
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def _bstHelper(nums):
            if not nums:
                return None
            node = TreeNode(nums[len(nums) // 2])
            node.left = _bstHelper(nums[:len(nums) // 2])
            node.right = _bstHelper(nums[len(nums) // 2 + 1:])
            return node
        root = _bstHelper(nums)
        return root
    
    # Time: O(n)
    # Space: O(n) - Really it's 3*n, since we store each node along
    #               with each right/left index
    # Iterative solution using stacks
    def sortedArrayToBST2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        head = TreeNode(None)
        nodeStack = [head]
        leftIndexStack = [0]
        rightIndexStack = [len(nums) - 1]
        while nodeStack:
            curNode = nodeStack.pop()
            left = leftIndexStack.pop()
            right = rightIndexStack.pop()
            mid = left + (right - left) // 2
            curNode.val = nums[mid]
            if left <= mid - 1:
                curNode.left = TreeNode(None)
                nodeStack.append(curNode.left)
                leftIndexStack.append(left)
                rightIndexStack.append(mid - 1)
            if mid + 1 <= right:
                curNode.right = TreeNode(None)
                nodeStack.append(curNode.right)
                leftIndexStack.append(mid + 1)
                rightIndexStack.append(right)
        return head


if __name__ == "__main__":
    import binaryTreeInorderTraversal
    arr = [-10,-3,0,5,9]
    obj = Solution()
    root = obj.sortedArrayToBST2(arr)
    print(binaryTreeInorderTraversal.Solution().inorderTraversal(root))

 
