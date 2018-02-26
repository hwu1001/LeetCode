# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

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
        while root:
            if root.left:
                nextNode = root.left
            elif root.right:
                nextNode = root.right
            else:
                nextNode = root.next

            while root:
                # Look down a level
                if root.left:
                    if root.right:
                        root.left.next = root.right
                    # Look across level to find next node
                    node = root.next
                    while node and not root.left.next:
                        if node.left:
                            root.left.next = node.left
                        elif node.right:
                            root.left.next = node.right
                        node = node.next
                if root.next and root.right:
                    # Look across level to find next node
                    node = root.next
                    while node and not root.right.next:
                        if node.left:
                            root.right.next = node.left
                        elif node.right:
                            root.right.next = node.right
                        node = node.next
                root = root.next
            root = nextNode

    # Time: O(n)
    # Space: O(1)
    # Mucher cleaner iterative solution than my original one above
    def connect2(self, root):
        tempChild = TreeLinkNode(0)
        while root:
            currentChild = tempChild
            # Look across level in this loop to set next nodes
            # Notice how the first node that has .left or .right set will be
            # tempChild.next. Then from then on it is just setting
            # actual nodes .next property
            while root:
                if root.left:
                    currentChild.next = root.left
                    currentChild = currentChild.next
                if root.right:
                    currentChild.next = root.right
                    currentChild = currentChild.next
                root = root.next
            # Move down a level to the left-most node of the level
            root = tempChild.next
            tempChild.next = None

if __name__ == "__main__":
    # root = TreeLinkNode(1)
    # root.left = TreeLinkNode(2)
    # root.right = TreeLinkNode(3)
    # root.left.left = TreeLinkNode(4)
    # root.left.right = TreeLinkNode(5)
    # root.right.left = TreeLinkNode(6)
    # root.right.right = TreeLinkNode(7)

    # root.right.left = TreeLinkNode(5)
    # root.left.left.left = TreeLinkNode(6)
    # root.right.left.left = TreeLinkNode(7)

    # root = TreeLinkNode(1)
    # root.left = TreeLinkNode(2)
    # root.right = TreeLinkNode(3)
    # root.left.left = TreeLinkNode(4)
    # root.left.right = TreeLinkNode(5)
    # root.left.left.left = TreeLinkNode(7)
    # root.right.right = TreeLinkNode(6)
    # root.right.right.right = TreeLinkNode(8)

    root = TreeLinkNode(-1)
    root.left = TreeLinkNode(-7)
    root.right = TreeLinkNode(9)
    root.right.left = TreeLinkNode(-1)
    root.right.right = TreeLinkNode(-7)
    root.right.left.right = TreeLinkNode(8)
    root.right.right.left = TreeLinkNode(-9)

    obj = Solution()
    obj.connect2(root)
    # Print left-most nodes of each level
    level = [root]
    while level:
        print(level[0])
        level = [child for node in level for child in (node.left, node.right) if child]