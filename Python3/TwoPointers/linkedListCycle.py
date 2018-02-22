# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time: O(n) - Note that if there is no cycle in the list then the time is truly O(n)
    #              since the hare will simply iterate through the list. If there is a cycle
    #              then the time is O(N + k) where N is the non-cycle lenght plus
    #              k, the cyclic length, since the pointers are moving at a difference speed of 1.
    #              That still converts to O(n)
    # Space: O(1)
    # Iterative solution using the tortoise and the hare algorithm (Two pointers)
    # https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
    # http://codingfreak.blogspot.com/2012/09/detecting-loop-in-singly-linked-list_22.html
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        tortoise = head
        hare = head
        # Could also just write
        # while hare and hare.next:
        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            # Because they're both classes we can use "is" keyword
            # Using == also works too though
            if tortoise is hare:
                return True
        return False


        # Original algorithm
        # while True:
        #     if hare is None:
        #         return False
        #     hare = hare.next
        #     if hare is None:
        #         return False
        #     hare = hare.next
        #     tortoise = tortoise.next
        #     if tortoise == hare:
        #         return True

    # Time: O(n)
    # Space: O(n)
    # Iterative solution using a hash table
    def hasCycle2(self, head):
        listData = set()
        while head:
            # Average case for in operation on set is O(1)
            # Worst case is O(n)
            if head in listData:
                return True
            else:
                listData.add(head)
            head = head.next
        return False
        
if __name__ is "__main__":
    from LinkedList import ListNode
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = first
    
    obj = Solution()
    print(obj.hasCycle(first))