# https://leetcode.com/problems/top-k-frequent-elements/description/

from heapq import heapify,heappush,heappop,nsmallest
from collections import Counter

class Solution(object):
    # Time: O(nlog(k)) - where k is the number of unique elements in n
    # Space: O(n)
    # Min heap solution
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        tupHeap = [(-value, key) for key, value in counter.items()]
        heapify(tupHeap)
        # Note that we could have alternatively stored the raw value and used heapq.nlargest()
        return [tup[1] for tup in nsmallest(k, tupHeap)]
    
    # Time:O(nlog(k)) - where k is the number of unique elements in n
    # Space: O(n)
    # Heap solution using only k most frequent values
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        topKHeap = []
        heapify(topKHeap)
        for key, value in counter.items():
            heappush(topKHeap, (value, key))
            if len(topKHeap) > k:
                heappop(topKHeap)
        return [tup[1] for tup in topKHeap]

    
    # Time: O(nlog(k))
    # Space: O(n) - Since .most_common() uses heapq.nlargest under the hood
    #               it will use log(n) space for the heap
    # Python Counter object solution
    # https://docs.python.org/3/library/collections.html#collections.Counter
    def topKFrequent3(self, nums, k):
        return [tup[0] for tup in Counter(nums).most_common(k)]
    
    # Time: O(n)
    # Space: O(n)
    # Bucket sort solution
    # https://en.wikipedia.org/wiki/Bucket_sort
    def topKFrequent4(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for key, freq in counter.items():
            bucket[freq].extend([key])
        revIndex = len(bucket) - 1
        ret = []
        while revIndex >= 0 and len(ret) < k:
            if bucket[revIndex] != []:
                ret.extend(bucket[revIndex][:k])
            revIndex -= 1
        return ret


if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]
    nums = [1,1,1,2,2,2,3,3,3]
    # nums = [1,2]
    obj = Solution()
    print(obj.topKFrequent4(nums,2))
