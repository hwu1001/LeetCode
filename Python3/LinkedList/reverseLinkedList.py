# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(n)
    # Space: O(1)
    # Iterative solution
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = None
        while head:
            # Doing this operation in one line so that we don't have to use an
            # additional temp variable. We're just going to reverse each node
            # as we iterate through the list
            rev, rev.next, head = head, rev, head.next
        # Since we've iterated through the entire list this return is the last
        # node from the original list
        return rev
    
    # Time: O(n)
    # Space: O(n) - since the list will be saved on the stack execution
    # Recursive solution
    def reverseListRecur(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            # Return the last node in the list all the way back to the beginning
            return head
        node = self.reverseListRecur(head.next)
        # In the present node, set the node after it from the original list
        # equal to the present node. (i.e., reverse the node ahead of the present one)
        head.next.next = head
        head.next = None
        return node

if __name__ == "__main__":
    from LinkedList import LinkedList
    linked = LinkedList()
    for c in "string":
        linked.add(c)
    
    print("Before")
    linked.displayList()
    
    obj = Solution()
    # linked.head = obj.reverseList(linked.head)
    linked.head = obj.reverseListRecur(linked.head)
    print("After")
    linked.displayList()
