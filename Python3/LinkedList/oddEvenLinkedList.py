# https://leetcode.com/problems/odd-even-linked-list/

from LinkedList import LinkedList, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(n)
    # Space: O(1) - Changing data in place instead of allocating new space
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

if __name__ == '__main__':
    obj = Solution()
    l = LinkedList()
    for num in [1,2,3,4,5]:
        l.add(num)
    n = obj.oddEvenList(l.head)
    for num in [1,3,5,2,4]:
        assert(num == n.val)
        n = n.next

    l2 = LinkedList()
    for num in [2,1,3,5,6,4,7]:
        l2.add(num)
    n = obj.oddEvenList(l2.head)
    for num in [2,3,6,7,1,5,4]:
        assert(num == n.val)
        n = n.next