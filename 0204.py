class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        all = [True] * n

        # scan only odd numbers
        result = 1
        for i in range(3, n, 2):
            if all[i] == False:
                continue

            result += 1

            # sieve
            j = 3*i
            while j < n:
                all[j] = False
                j += 2*i

        return result
