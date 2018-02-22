# https://leetcode.com/problems/plus-one/description/
# The prompt is a bit confusing so here's what they really mean:
# suppose you have a number in your list/array such that adding 1 would make it a two digit number,
# eg: [9]
# o/p: [1,0]
# Plusone(9) would be [10], but the expected output should be [1,0] such that the most significant digit is on the head
# 
# [1, 2, 3, 4] represents integer 1234, add one to 1234(the length of array not changed), you get 1235. 
# but [9, 9, 9, 9] represents 9999, add one to 9999, you get 10000(the length of array changed)

class Solution:
    # Time: O(n)
    # Space: O(n) - since we're generating a new list to return
    #               in our list comprehension
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits))) + 1
        return [int(digit) for digit in str(num)]
    
    # Time: O(n)
    # Space: O(1) - Since we're altering the list in place
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == "__main__":
    digits = [9,9,9,9]
    obj = Solution()
    print(obj.plusOne(digits))
