class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def add(self, data):
        if (self.isEmpty()):
            self.head = ListNode(data)
        else:
            node = self.head
            while (node.next != None):
                node = node.next
            node.next = ListNode(data)
        return

    def isEmpty(self):
        return self.head == None
    
    def displayList(self):
        node = self.head
        while (node):
            print(node.val)
            node = node.next
        return

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None