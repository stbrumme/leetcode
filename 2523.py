class Solution:
    cache = {}
    def isPrime(self, n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2

        if self.cache.get(n):
            return self.cache[n]

        prime = True
        i = 3
        while i*i <= n:
            if n % i == 0:
                prime = False
                break
            i += 2

        self.cache[n] = prime
        return prime


    def closestPrimes(self, left: int, right: int) -> List[int]:
        result = [ -1, -1 ]
        found = False
        for i in range(left, right):
            if not self.isPrime(i):
                continue
            for j in range(i+1, right+1):
                if self.isPrime(j):
                    diff = j - i
                    if not found or diff < result[1] - result[0]:
                        result = [ i, j ]
                        found = True

                        # can't be better
                        if diff == 2:
                            return result
                    break

        return result
