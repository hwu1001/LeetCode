# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from LinkedList import LinkedList, ListNode

class Solution(object):
    # Time: O(n)
    # Space: O(1)
    # Two pointer solution with single loop
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        node = head
        trailing = head
        count = 1
        while (node):
            if count > n:
                prev = trailing
                trailing = trailing.next
            node = node.next
            count += 1
        # If we're given a bad input for n do nothing, return the head
        if n >= count:
            return head
        # If count minus one is equal to n, we're deleting the head
        elif count - 1 == n:
            del head
            return trailing.next
        # Otherwise, n is less than count - 1, which means we're somewhere after the head
        else:
            prev.next = trailing.next
            del trailing
        return head

    # Time: O(n)
    # Space: O(1)
    # This effectively does the same, but uses two loops. It's the really the same
    # amount of work, I think the two loops might just be frowned upon?
    # In this solution we have two pointers but the first pointer is given a lead
    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n + 1):
            if first == None:
                return head
            first = first.next
        while (first != None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

if __name__ == "__main__":
    linked = LinkedList()
    linked.add(1)
    linked.add(2)
    linked.add(3)
    linked.add(4)
    linked.add(5)
    
    print("Before")
    linked.displayList()

    print("After")
    obj = Solution()
    linked.head = obj.removeNthFromEnd2(linked.head, 5)
    linked.displayList()