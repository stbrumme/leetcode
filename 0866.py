class Solution:
    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2

        # generator for all palindromes
        def palindromes():
            i   = 0
            odd = True
            threshold = 10
            while True:
                # one more digit
                if i == threshold:
                    if odd:
                        # reset count but allow one more digit in the second half
                        i //= 10
                        odd = False
                    else:
                        # increase threshold, skip middle digit
                        odd = True
                        threshold *= 10

                # build palindrome
                one = str(i)
                two = one[::-1]
                if odd:
                    two = two[1:]
                yield int(one + two)

                i += 1

        for x in palindromes():
            if x >= n and (x & 1) == 1: # skip even palindromes because they can't be primes
                # basic prime test
                p = 3
                prime = True
                while p*p <= x:
                    if x % p == 0:
                        prime = False
                        break
                    p += 2

                if prime:
                    return x
