class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # convert all to the same denominator
        primes = [ 2 ]
        for n in range(3, 1000, 2):
            i = n
            for j in primes:
                while i % j == 0:
                    i //= j
            if i > 1:
                primes.append(n)

        de = 1
        for i in primes:
            de *= i

        all = { }
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                ii = arr[i]
                jj = arr[j]
                scaled = ii * de // jj
                all[scaled] = [ ii, jj ]

        keys = sorted(all.keys());
        return all[keys[k-1]]
