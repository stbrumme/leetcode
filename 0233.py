class Solution:
    # chop off a single digit per round
    @cache
    def compute(self, n):
        if n == 0:
            return 0
        if n < 10:
            return 1

        # process highest digit first

        s = str(n)
        first = int(s[0])
        withoutFirst = 0
        digits = len(s)
        if digits > 1:
            withoutFirst = int(s[1:])

        shift = 10**(digits - 1)
        # e.g. if n = 345 => first = 3, shift = 100, digits = 2, withoutFirst = 45

        # brute-force results:
        # < 10 => 1
        # < 100 => 20
        # < 1000 => 300
        # < 10000 => 4000
        # < 100000 => 50000
        # ...
        result = first * (digits - 1) * shift // 10

        if first > 1:
            result += shift
        else:
            result += withoutFirst + 1 # initial 1 appears for each number

        # count 1s for n without its first digit
        result += self.compute(withoutFirst)

        return result

    def countDigitOne(self, n: int) -> int:
        return self.compute(n)
