from LinkedList import LinkedList,ListNode
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(n)
    # Space: O(1)
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # If either list is empty return the other list
        if not l1:
            return l2
        if not l2:
            return l1
        # Use newList for return and curNode for processing each node in the list
        newList = curNode = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        # Append the list that still has data to the end
        # All the values will be the largest
        if l1:
            curNode.next = l1
        else:
            curNode.next = l2
        # The or operator in assignment takes the first value that evaluates to True
        # and returns it. It's equivalent to the above if/else in this case
        # curNode.next = l1 or l2
        return newList.next
        
    # Not including the recursive solution since it is generally not practical. The reason
    # being is that the recursive depth will be the length of the list, which means the stack 
    # will overflow for relatively small lists.

if __name__ == "__main__":
    linked1 = LinkedList()
    linked2 = LinkedList()
    for i in [1,2,5]:
        linked1.add(i)
    
    for j in [1,3,4]:
        linked2.add(j)
    print("before list 1")
    linked1.displayList()
    print("before list 2")
    linked2.displayList()

    print("After")
    obj = Solution()
    merge = LinkedList()
    merge.head = obj.mergeTwoLists(linked1.head, linked2.head)
    merge.displayList()

