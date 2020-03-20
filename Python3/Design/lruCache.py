# https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return "(key: " + str(self.key) + " val: " + str(self.val) + ")"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, node: ListNode) -> None:
        node.next, node.prev = None, None
        if self.tail is None:
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node
    
    def remove(self, node: ListNode) -> None:
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
    
    def display(self) -> None:
        node = self.head
        while node:
            print(node.key, node.val)
            node = node.next

        

class LRUCache:

    def __init__(self, capacity: int):
        self.list = DoublyLinkedList()
        self.map = {}
        self.capacity = capacity
    
    def _updateCache(self, key: int, val: int) -> None:
        node = ListNode(key, val)
        self.list.prepend(node)
        self.map[key] = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self._updateCache(node.key, node.val)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.list.remove(self.map[key])
            self._updateCache(key, value)
        else:
            if len(self.map) == self.capacity:
                tail = self.list.tail
                del self.map[tail.key]
                self.list.remove(tail)
            self._updateCache(key, value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.map)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.map)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    # n1 = ListNode(1, 1)
    # n2 = ListNode(2, 2)
    # n3 = ListNode(3, 3)
    # dl = DoublyLinkedList()
    # dl.prepend(n3)
    # dl.prepend(n2)
    # dl.prepend(n1)
    # dl.display()
    # print('delete')
    # dl.remove(n1)
    # dl.display()