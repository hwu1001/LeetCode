# https://leetcode.com/problems/kth-smallest-element-in-a-bst/ 

# For the part about if the BST is modified(insert/delete operations) often and 
# the kth smallest is needed frequently. For this we could use a BST with a 
# doubly-linked list (similar to LRU cache design)
# The structure could provide:
# O(h) time for insert/delete
# O(k) time for kth smallest element
# That way the time complexity for insert/delete + kth smallest element would be
# O(h + k) instead of O(2h + k). Average case would be O(logn + k), O(n + k) worst case
# Space complexity would be O(n) for the linked list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from treeVisualizer import deserialize, TreeNode

class Solution:
    # Inorder traversal
    # Time: O(h + k) - where h is the height of the tree
    # Space: O(h + k)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []
        count = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
        return -1

class Solution2:
    # Time: O(n) - traverses all the elements in the tree
    # Space: O(h)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                self.count -= 1
                if self.count == 0:
                    self.res = node.val
                    return
                inorder(node.right)

        self.count = k
        self.res = -1
        inorder(root)
        return self.res

if __name__ == '__main__':
    obj = Solution()
    root = deserialize('[3,1,4,null,2]')
    assert(obj.kthSmallest(root, 1) == 1)
    root2 = deserialize('[5,3,6,2,4,null,null,1]')
    assert(obj.kthSmallest(root2, 3) == 3)
    assert(obj.kthSmallest(root2, 6) == 6)
    root3 = deserialize('[5,null,6,null,7]')
    assert(obj.kthSmallest(root3, 2) == 6)