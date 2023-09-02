class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])

        if c % a == 0 or c % b == 0:
            c = 10**10 # larger than any result
        if b % a == 0:
            b, c = c, 10**10

        ab = a*b // gcd(a, b)
        bc = b*c // gcd(b, c)
        ac = a*c // gcd(a, c)
        abc = a*b*c // gcd(a, b, c)

        def ugly(guess):
            one = guess // a  + guess // b  + guess // c
            two = guess // ab + guess // bc + guess // ac
            three = guess // abc
            return one - two + three

        result = n * a
        step   = result // 2
        while step > 1:
            if ugly(result) >= n:
                result -= step
            else:
                result += step

            step //= 2

        while ugly(result) >= n:
            result -= 1
        while ugly(result) < n:
            result += 1

        return result
