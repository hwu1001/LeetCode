# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    # Time: O(3^n * 4^m) - where n is is the number of digits with 3 letters and
    #                      m is the number of digits with 4 letters
    # Space: O(3^n * 4^m)
    def letterCombinations(self, digits: str) -> List[str]:
        # The letters are purposefully reversed so the solution is
        # lexographically sorted
        digits_to_letters = {
            '2': 'cba',
            '3': 'fed',
            '4': 'ihg',
            '5': 'lkj',
            '6': 'onm',
            '7': 'srqp',
            '8': 'vut',
            '9': 'zyxw'
        }
        if len(digits) < 1:
            return []
        stack = [[c] for c in digits_to_letters[digits[0]]]
        ans = []
        while stack:
            phone_number = stack.pop()
            number_len = len(phone_number)
            if number_len == len(digits):
                ans.append(''.join(phone_number))
            else:
                for c in digits_to_letters[digits[number_len]]:
                    number_copy = phone_number[:]
                    number_copy.append(c)
                    stack.append(number_copy)
        return ans

class Solution2:
    # Recursive solution
    # Time: O(3^n * 4^m) - where n is is the number of digits with 3 letters and
    #                      m is the number of digits with 4 letters
    # Space: O(3^n * 4^m)
    def letterCombinations(self, digits: str) -> List[int]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack('', digits)
        return output

if __name__ == '__main__':
    obj = Solution()
    sol1 = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert(obj.letterCombinations('23') == sol1)
    sol2 = ['ap', 'aq', 'ar', 'as', 'bp', 'bq', 'br', 'bs', 'cp', 'cq', 'cr', 'cs']
    assert(obj.letterCombinations('27') == sol2)

        