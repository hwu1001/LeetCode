# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LinkedList import ListNode, LinkedList

class Solution:
    # Time: O(n)
    # Space: O(n)
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next
        return arr[len(arr) // 2]

    # Time: O(n)
    # Space: O(1)
    def middleNode2(self, head: ListNode) -> ListNode:
        mid = head
        count = 0
        while head:
            if count % 2:
                mid = mid.next
            count += 1
            head = head.next
        return mid

    # Time: O(n)
    # Space: O(1)
    def middleNode3(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    # l = [1,2,3,4,5]
    l = [1,2,3,4,5,6]
    ll = LinkedList()
    for val in l:
        ll.add(val)
    
    obj = Solution()
    print(obj.middleNode(ll.head).val)