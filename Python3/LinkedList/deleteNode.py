# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time: O(1)
    # Space: O(1)
    # For languages with garbage collection simply, turn your current
    # node into the next node and let the next node be garbage collected
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return