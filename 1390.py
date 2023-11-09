class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0

        for n in nums: # 6 is the smallest number with 4 divisors
            # i is always divisble by 1 and itself
            total = 1 + n
            found = 2

            # square numbers always have an odd number of divisors
            s = sqrt(n)
            if s == int(s):
                continue

            # factorize
            for factor in range(2, int(s) + 1):
                if n % factor == 0:
                    found += 2
                    if found > 4:
                        break # too many

                    other = n // factor
                    total += factor + other

            # match
            if found == 4:
                result += total

        return result
