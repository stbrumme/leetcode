class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        odd = (n + 1) // 2
        isprime = [ True ] * odd
        isprime[0] = False
        # basic sieve for odd numbers
        for i in range(3, n, 2):
            if isprime[i >> 1]:
                for j in range(i*i, n, 2*i):
                    isprime[j >> 1] = False

        if n % 2 == 1 or n == 4:
            if isprime[(n - 2) >> 1]:
                return [[ 2, n - 2 ]]
            return []

        result = []
        for i in range(3, n // 2 + 1, 2):
            if isprime[i >> 1] and isprime[(n - i) >> 1]:
                result.append([ i, n - i ])
        return result
