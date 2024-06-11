class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # if n ==  99 then there are  10 numbers between 1 and 2 (and  10 between 2 and 3, 3 and 4, ...)
        # if n == 999 then there are 100 numbers between 1 and 2 (and 100 between 2 and 3, 3 and 4, ...)
        # ...
        result = 1

        k -= 1
        while k > 0:
            start   = result
            end     = result + 1
            # count numbers between start and end (in lexicographical order)
            covered = 0

            while start <= n:
                covered += min(end, n + 1) - start
                start   *= 10
                end     *= 10

            if covered > k:
                result *= 10
                k      -= 1
            else:
                result += 1
                k      -= covered

        return result
