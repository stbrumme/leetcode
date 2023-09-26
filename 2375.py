class Solution:
    def smallestNumber(self, pattern: str) -> str:
        @cache
        def deeper(have):
            if len(have) == len(pattern) + 1:
                return have

            previous = int(have[-1])
            if pattern[len(have) - 1] == "I":
                low  = previous + 1
                high = 10
            else:
                low  = 1
                high = previous

            for i in range(low, high):
                if str(i) not in have:
                    result = deeper(have + str(i))
                    if result:
                        return result
            return None

        # first digit
        for i in range(1, 10):
            result = deeper(str(i))
            if result:
                return result
