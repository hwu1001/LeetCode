# https://leetcode.com/problems/count-primes/description/

class Solution:
    # Time: O(n)
    # Space: O(n)
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = [Solution.isPrime(value) for value in range(0, n)]
        # If n = 2, the prime 2 is not less than n,
        # so there are no primes less than n
        if n < 3:
            return 0

        # We know that 0 and 1 are not prime, mark all others as
        # potentials that we'll eliminate with the sieve algorithm
        # below
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        # Our iteration will not exceed sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):
            # With this check we can find the next number that isn't considered prime yet
            # otherwise we skip the number by restarting the loop
            if primes[i]:

                # See below commented out code of the for-loop for a more detailed
                # explanation of what is happening below. You can set a slice of our list
                # of primes and step through it to implement the part of the sieve
                # that determines all multiples of a given number are not prime numbers 
                # NOTE: I use len(range(i * i, n, i)) instead of len(primes[i * i : n : i]) since it
                # has the same effect and is faster. The primes list holds the same data that range()
                # returns, but in this way there's no need for Python to slice the list then determine the length
                primes[i * i : n : i] = [False] * len(range(i * i, n, i))

                # primes[i * i : n : i] = [False] * len(primes[i * i : n : i])
                # for j in range(i * i, n, i):
                #     primes[j] = False
        return sum(primes)
    
    # Time: O(n)
    # Space: O(n)
    # This solution will be slower than the one with list slicing
    def orig_sieve(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes)

    @staticmethod
    def isPrime(value):
        if (value < 2): return False
        if (value == 2): return True
        if (value % 2 == 0): return False

        i =  3
        while (i < int(value ** 0.5) + 1):
            if (value % i == 0): return False
            i += 1
        return True

    def countPrimes2(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    # This method is slower in Python than countPrimes and countPrimes2 - likely because list slicing is faster than a standard loop
    def countPrimes3(self, n):
        if (n < 3):
            return 0
        c = n // 2
        s = [False] * n
        i = 3
        while (i * i < n):
            if (s[i]):
                i += 2
                continue
            for j in range(i * i, n, 2 * i):
                if not s[j]:
                    c -= 1
                    s[j] = True
            i += 2
        return c

if __name__ == '__main__':
    # 499979
    obj = Solution()
    print(obj.orig_sieve(499979))
    