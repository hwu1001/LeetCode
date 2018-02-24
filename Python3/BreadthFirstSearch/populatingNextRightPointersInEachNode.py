# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    
    def __repr__(self):
        if self is None:
            return "Null"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # Time: O(n)
    # Space: O(1)
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                root = root.next
            root = next
    
    # The problem calls for constant space, but still
    # good to know the recursive solution
    # Time: O(n)
    # Space: O(log(n)) - We only have half the tree in the execution stack
    #                    at any given time
    def connectRecur(self, root):
        if root is None:
            return
        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
        self.connectRecur(root.left)
        self.connectRecur(root.right)

if __name__ == "__main__":
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)
    obj = Solution()
    obj.connectRecur(root)
    node = root
    while node:
        print(node)
        if node.left:
            node = node.left
        elif node.right:
            node = node.right
        else:
            node = None