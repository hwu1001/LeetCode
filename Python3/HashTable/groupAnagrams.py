# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

class Solution:
    # Time: O(n * klog(k)) - Where n is the length of strs and k is the maximum length of
    #                        a string in strs. We're iterating over strs so it takes n time
    #                        and then sorting each string which is klog(k) time.
    # Space: O(n * k)
    # Categorize anagrams by sorted string
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        anagramIndices = {}
        anagrams = []
        index = 0
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in anagramIndices:
                anagrams[anagramIndices[sortedStr]].append(s)
            else:
                anagramIndices[sortedStr] = index
                anagrams.append([])
                anagrams[index].append(s)
                index += 1
        return anagrams

    # Time: O(n * klog(k))
    # Space: O(n * k)
    # Categorize anagrams by sorted string
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        ret = {}
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr not in ret:
                ret[sortedStr] = []
            ret[sortedStr].append(s)
        return [anagramList for anagramList in ret.values()]
    
    # Time: O(n * k) - where k is the maximum length of a string in strs
    # Space: O(n * k) 
    # Categorize by character count
    def groupAnagrams3(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        ret = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ret[tuple(count)].append(s)
        return list(ret.values())
        

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    obj = Solution()
    print(obj.groupAnagrams(words))
