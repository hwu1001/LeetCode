# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time: O(m + n)
    # Space: O(m) or O(n)
    # Hash table solution
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        if headA == headB:
            return headA
        seenNodes = {}
        while headA:
            seenNodes[headA] = 1
            headA = headA.next
        while headB:
            if headB in seenNodes:
                return headB
            headB = headB.next
        return None
    
    # Time: O(m + n)
    # Space: O(1)
    # Two pointer solution
    def getIntersectionNode2(self, headA, headB):
        if not headA or not headB:
            return None
        ptrA, ptrB = headA, headB
        # There will be two traversals in this loop if
        # the two lists are different in length
        while ptrA != ptrB:
            # By redirecting the pointers to the other list we guarantee
            # that the lists will reach their intersection point at the same time
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA

if __name__ == "__main__":
    from LinkedList import ListNode
    a = ListNode("1a")
    a.next = ListNode("2a")

    b = ListNode("1b")
    b.next = ListNode("2b")
    b.next.next = ListNode("3b")
    
    c = ListNode("1c")
    c.next = ListNode("2c")
    c.next.next = ListNode("3c")

    a.next.next = c
    b.next.next.next = c

    obj = Solution()
    node = obj.getIntersectionNode2(a, b)
    if node:
        print(node.val)
    else:
        print(node)


