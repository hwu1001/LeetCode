# https://leetcode.com/problems/task-scheduler/description/

from collections import Counter
from queue import PriorityQueue
class Solution:
    # Time: O(n)
    # Space: O(1)
    # This solution determines the number of idle slots needed with the
    # given cooling time/tasks. Consider the following tasks:
    # "AAABBB" with cooling period of 2 (n = 2). 0 is idle slot
    # A B 0
    # A B 0
    # A B
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskCounts = Counter(tasks).values()
        # Get the count of the most frequent task
        maxTaskCount = max(taskCounts)
        # Get the number of tasks that match the largest count value
        numModes = list(taskCounts).count(maxTaskCount)
        # For instances where there are several modes, it's possible to have fewer steps
        # than tasks given, usually when n is very small. Otherwise, we want to return
        # maxTask-<other tasks or idle> times the length of the interval plus one 
        # since that's how the interval will split the pattern into that many instances.
        # For maxTaskCount - 1, it's considering the spots available to do tasks and minus one
        # since we know the first one is the max task. Add the number of modes to the end since
        # those will be used exclusively once the other tasks are exhausted
        return max((maxTaskCount - 1) * (n + 1) + numModes, len(tasks))
    
    # Time: O(n) - Iterating over tasks once to get the count
    #              Sorting the tasks which has O(26log(26)) = O(1) time.
    #              Then iterating once more over the 26 elements that counted
    #              the number of tasks
    # Space: O(1)
    # Same as other idle slot calculation, but framed in a bit of a different
    # way
    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Our tasks can only be upper-case letters from A to Z
        # so we can take that to do some constant time operations
        taskCounter = [0] * 26
        for c in tasks:
            taskCounter[ord(c) - ord("A")] += 1
        taskCounter.sort()
        # We subtract one from maxVal because in the last round of execution
        # of tasks the idle slots are not needed
        maxVal = taskCounter[25] - 1
        idleSlots = maxVal * n
        i = 24
        while(i >= 0 and taskCounter[i] > 0):
            # Replace the placeholder idle slots with the
            # tasks. We need to do min() here because
            # there could be multiple maxVal tasks and if 
            # there are then we'd need to subtract 1 from those
            # as well
            idleSlots -= min(taskCounter[i], maxVal)
            i -= 1
        if idleSlots > 0:
            return idleSlots + len(tasks)
        else:
            return len(tasks)

    # Time: O(n)
    # Space: O(1) - since the priority queue, temp storage, and taskCounter
    #               will not exceed 26
    # Solution using a max-heap priority queue
    def leastInterval3(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskCounter = [0] * 26
        for c in tasks:
            taskCounter[ord(c) - ord("A")] += 1
        queue = PriorityQueue()
        for val in taskCounter:
            if val > 0:
                # We want to create a reverse order priority queue
                # where the maximum is at the front so store a tuple
                # with (priority number, data)
                queue.put((-val, val))
        time = 0
        while(not queue.empty()):
            i = 0
            temp = []
            while(i <= n):
                if (not queue.empty()):
                    # There's no .peek() in Python priority quues
                    if queue.queue[0][1] > 1:
                        temp.append(queue.get()[1] - 1)
                    else:
                        # Once there's only one execution of a task left
                        # no need to append to temp since it requires no
                        # idle time
                        queue.get()
                time += 1
                if (queue.empty() and len(temp) == 0):
                    break
                i += 1
            for val in temp:
                queue.put((-val, val))
        return time

if __name__ == "__main__":
    # t = ["A","A","A","B","B","B"]
    # t = ["A","A","A","A","B","C","D","E"]
    t = ["A","A","A","A","B","B","B","C","C","D"]
    obj = Solution()
    print(obj.leastInterval2(t, 3))
    
    # Some additional examples (where ~ is idle slot)
    # This formula becomes much clearer:
    # max((maxTaskCount - 1) * (n + 1) + numModes, len(tasks))
    #   (maxTaskCount - 1) - the number of rows in the rectangle
    #                        where we need idle slots or other tasks
    #   (n + 1)            - the number of columns in the rectangle
    #                        where idle slots will exist (add 1) because
    #                        we need to include the most frequently occurring
    #                        task in addition to the period n, that we have to
    #                        wait before doing it again
    #   numModes           - Only the most frequently occuring tasks will appear
    #                        on the final row and there could be more than one
    
    # AAAABBBCCD, n = 3

    # A B C D
    # A B C ~
    # A B ~ ~
    # A

    # AAAA, n = 2

    # A ~ ~ 
    # A ~ ~
    # A ~ ~
    # A