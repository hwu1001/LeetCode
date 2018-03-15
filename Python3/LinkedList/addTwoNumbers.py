# https://leetcode.com/problems/add-two-numbers/description/

from LinkedList import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(n)
    # Space: O(n)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumList = ListNode(None)
        dummy = sumList
        carry = 0
        # Keep iterating until both lists are exhausted
        while l1 or l2:
            nodeVal1 = 0
            nodeVal2 = 0
            if l1:
                nodeVal1 = l1.val
                l1 = l1.next
            if l2:
                nodeVal2 = l2.val
                l2 = l2.next
            nodeSum = nodeVal1 + nodeVal2 + carry
            if nodeSum >= 10:
                nodeSum = nodeSum % 10
                carry = 1
            else:
                carry = 0
            sumList.next = ListNode(nodeSum)
            sumList = sumList.next
        # Carry the last sum if necessary
        if carry != 0:
            sumList.next = ListNode(carry)
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(None)
    dummy1 = l1
    l2 = ListNode(None)
    dummy2 = l2
    for val in [2,4,3]:
        l1.next = ListNode(val)
        l1 = l1.next
    for val in [5,6,4]:
        l2.next = ListNode(val)
        l2 = l2.next
    obj = Solution()
    ret = obj.addTwoNumbers(dummy1.next, dummy2.next)
    while ret:
        print(ret.val)
        ret = ret.next
        