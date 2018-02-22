# https://leetcode.com/problems/min-stack/description/

# Implementation using a linked list and O(1) operations, except
# if the minimum is popped from the stack

# Time: O(n) - Note that if the min value is popped, the operation
#              does not run in constant time as the entire stack needs
#              to be traversed in order to find a new min. All other operations
#              are O(1)
# Space: O(n)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topNode = None
        self.minNode = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        isEmpty = self.isEmpty()
        self.topNode = StackNode(x, self.topNode)
        if isEmpty:
            self.minNode = self.topNode
        elif x < self.minNode.val:
            self.minNode = self.topNode

    def pop(self):
        """
        :rtype: void
        """
        if self.isEmpty():
            return
        if self.minNode == self.topNode:
            node = self.topNode.next
            self.minNode = node
            while(node):
                if node.val < self.minNode.val:
                    self.minNode = node
                node = node.next

        self.topNode = self.topNode.next
        

    def top(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return None
        return self.topNode.val
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return None
        return self.minNode.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.topNode is None

class StackNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time: O(1) - This implementation is truly O(1) operations throughout
# Space: O(n)
class MinStack2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.isEmpty():
            self.stack.append(0)
            self.min = x
        else:
            # We'll push a negative value onto the stack if the min
            # value needs to change
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if self.isEmpty():
            return
        popVal = self.stack.pop()
        # If value is negative it means a min value is being popped off
        # the stack and we need to find the next min value.
        # We reverse what happened in push() to restore
        # the previous min value
        if popVal < 0:
            self.min = self.min - popVal
        # An example of the above is that popVal is what we previously
        # pushed onto the stack (and if it's a new min it's a negative value) so:
        #   popVal = curMin - prevMin
        # So to solve for prevMin (but remember popVal is negative, 
        # so really we're adding):
        #   prevMin = curMin - popVal

    def top(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return None
        topVal = self.stack[-1]
        if topVal > 0:
            return topVal + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return None
        return self.min
    
    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.stack == []

if __name__ == "__main__":
    obj = MinStack2()
    # obj.push(0)
    # obj.push(-2)
    # obj.push(-3)

    obj.push(3)
    obj.push(4)
    obj.push(2)
    obj.push(5)
    obj.push(1)

    print(obj.getMin())
    print(obj.top())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())