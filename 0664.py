class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def deeper(what, left, right):
            # empty/invalid substring
            if left > right:
                return 0

            # print the first character
            stamp = s[left]
            # remove leading and trailing positions with the stamped character
            while left < right and s[left + 1] == stamp:
                left  += 1
            while left < right and s[right]    == stamp:
                right -= 1

            # single character
            if left == right:
                return 1

            # the stampede begins ...
            best = 1 + deeper(what, left + 1, right)

            # locate the same character inside the string
            for i in range(left + 1, right):
                if s[i] == stamp:
                    a = deeper(what, left, i - 1)
                    b = deeper(what, i + 1, right)
                    best = min(best, a + b)

            return best

        return deeper(s, 0, len(s) - 1)
