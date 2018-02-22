# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(n)
    # Space: O(1)
    # Iterative solution reversing half of the list
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        tail = None
        lead = head
        while lead and lead.next:
            lead = lead.next.next
            # Doing this operation in one line to avoid using temporary variables
            rev, rev.next, head = head, rev, head.next

        # Handle odd numbered words by moving tail one more forward so rev and tail are the same length
        if lead:
            tail = head.next
        else:
            tail = head
        # tail = head.next if lead else head
        isPalindrome = True
        while rev:
            if rev.val != tail.val:
                isPalindrome = False
                # Don't break since we have to revert head to its original state
            head, head.next, rev = rev, head, rev.next
            # Keep moving down the tail that started in the first loop, while head moves in reverse 
            # reinstating the original links as it goes
            tail = tail.next
        return isPalindrome
    
    # Time: O(n)
    # Space: O(n)
    # This was my first idea, or a variant of it (you can either list slice or 
    # iterate through the string forwards and backwards at the same time to compare)
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s == s[::-1]

if __name__ == "__main__":
    from LinkedList import LinkedList
    linked = LinkedList()
    for c in "tatat":
        linked.add(c)

    print("Before")
    linked.displayList()

    obj = Solution()
    res = obj.isPalindrome(linked.head)
    print("after")
    linked.displayList()
    print(res)

