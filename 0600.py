class Solution:
    def findIntegers(self, n: int) -> int:
        high = "{0:b}".format(n)
        size = len(high)

        @cache
        def deeper(pos, prev, limit): # ( digits still needed, previous digit, upper limit )
            if pos == size:
                return 1

            # append "0"
            result = deeper(pos + 1, 0, limit and high[pos] == "0") # could remove limit

            # append "1" only if not preceded by "1"
            if prev != 1:
                if high[pos] == "1" or not limit: # do not exceed the upper limit, too
                    result += deeper(pos + 1, 1, limit)

            return result

        return deeper(0, 0, True)
