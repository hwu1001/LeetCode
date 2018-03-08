# https://leetcode.com/problems/largest-number/description/

from functools import cmp_to_key

class LargestNumberComparator(str):
    def __lt__(self, other):
        return self + other > other + self # with this our local maximum makes our global maximum

class Solution:
    # Time: O(nlog(n)) - since the Python sorted method has time complexity of nlogn
    # Space: O(n)
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largestNumStr = "".join(sorted(map(str, nums), key=LargestNumberComparator))
        if largestNumStr[0] == "0":
            return "0"
        else:
            return largestNumStr


# Alternative method using the transition function of functools.cmp_to_key
# This method is used since .sort() and sorted() in Python 3 do not have the cmp
# parameter anymore. 
# https://docs.python.org/3/library/functools.html#functools.cmp_to_key
# https://docs.python.org/3/library/functions.html#sorted
# Time: O(nlog(n))
# Space: O(n)
class Solution2:
    @staticmethod
    def compare(x, y):
        option_1 = x + y
        option_2 = y + x
        if option_1 > option_2:
            return 1
        elif option_1 == option_2:
            return 0
        return -1

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numStrs = [str(num) for num in nums]

        return ''.join(sorted(numStrs, key=cmp_to_key(self.compare), reverse=True)).lstrip("0") or "0"

if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    obj = Solution()
    print(obj.largestNumber(nums))


