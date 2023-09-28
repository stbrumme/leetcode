class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def makebase(n, base):
            if base == 2: # a bit faster than my code
                return bin(n)[2:]

            result = 0
            shift  = 1
            while n > 0:
                result += shift * (n % base)
                n     //= base
                shift  *= 10
            return result

        # minor cheating ... precomputed approx. highest half-side of palindromes for n=30 for each k
        limits = [ 0,0,94000,8400,520000,122000,5000,650000,5600,2500]

        # generate palindromes in base-10
        numbers = []
        for i in range(1, limits[k] * n // 30 + 2000):
            s = str(i)
            even = s + s[::-1]
            odd  = s[:-1] + s[::-1]
            numbers.append(int(even))
            numbers.append(int(odd))
        numbers.sort()

        result = 0
        count  = 0
        for i in numbers:
            b = str(makebase(i, k))
            if b == b[::-1]:
                result += i
                count  += 1
                if count == n:
                    break

        return result
