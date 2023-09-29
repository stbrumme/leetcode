class Solution:
    def minDays(self, n: int) -> int:
        dp  = set([n])
        day = 0
        while True:
            next = set()
            for x in dp:
                # last day: always eat one orange
                if x == 1:
                    return day + 1

                next.add(x - 1) # strategy A: eat one

                # strategy B: eat half
                if x % 2 == 0:
                    next.add(x // 2)

                # strategy C: eat two thirds
                if x % 3 == 0:
                    next.add(x // 3)

            dp = next
            day += 1
