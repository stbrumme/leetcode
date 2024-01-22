class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        result = 0

        have   = [] # min-heap, ordered by day of decay
        today  = -1 # current day, incremented at start of loop => first day is 0
        while True:
            today += 1

            # add fresh apples
            if today < len(apples) and apples[today] > 0:
                heappush(have, ( today + days[today], apples[today] ))

            # remove rotten apples
            while have and have[0][0] <= today:
                heappop(have)

            # no more apples
            if not have:
                # there will be more apples some day
                if today < len(apples):
                    continue

                return result

            # eat an apple
            decay, num = heappop(have)
            result += 1
            num    -= 1
            # put back remaining apples
            if num > 0:
                heappush(have, ( decay, num ))
