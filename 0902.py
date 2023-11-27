class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)

        # single digit
        if n < 10:
            return sum([ 1 if d <= s else 0 for d in digits ])

        # numbers with less digits than n can be generated without restrictions
        result = 0
        for i in range(1, len(s)):
            result += len(digits) ** i

        # for each digit d smaller than the first digit of n
        # we can generate all numbers with len(n) - 1 digits
        for i in range(len(s)):
            remaining = (len(s) - 1) - i
            for d in digits:
                if d < s[i]: # but not d == s[i] !!!
                    result += len(digits) ** remaining
            if s[i] not in digits:
                # no more restrictions
                break

            if remaining == 0: # and s[i] in digits
                result += 1 # the only case where d == s[i] is counted

        return result
