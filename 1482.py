class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        complete = [] # max(bloomDay[i : i + k])

        # compute complete[]
        last = [] # max-heap
        for right, b in enumerate(bloomDay):
            heappush(last, ( -b, right )) # negate because max-heap

            left = right - k + 1
            if left < 0:
                continue

            # remove flowers from heap if too far away
            while last[0][1] < left:
                heappop(last)

            complete.append(-last[0][0]) # negate because max-heap

        # greedily count bouquets on a given day
        def bouquets(day):
            nonlocal complete, k, m
            pick = 0
            pos  = 0
            while pos < len(complete):
                if complete[pos] <= day:
                    pos  += k    # skip flowers used for current bouquet
                    pick += 1

                    if pick > m: # early exit: enough bouquets
                        break
                else:
                    pos  += 1
            return pick

        earliest = min(complete)
        latest   = max(complete)
        day = earliest + bisect_left(range(earliest, latest + 1), m, key = bouquets)
        return day if day <= latest else -1
