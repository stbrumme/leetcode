class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # highest digit per cost
        high = {}
        for i, c in enumerate(cost, 1):
            high[c] = i
        # ordered (by cost)
        digits = []
        for h in sorted(high):
            digits.append(( str(high[h]), h ))

        @cache
        def deeper(price):
            if price == 0:
                return "" # found a valid number

            best = ""
            for digit, dollars in digits:
                if dollars > price:
                    break

                # append more digits
                next = deeper(price - dollars)
                # failed, target not met
                if next == None:
                    continue

                have = digit + next
                # longer than before
                if len(have) >  len(best):
                    best = have
                # same length but higher digits
                if len(have) == len(best):
                    best = max(best, have)

            return best if best else None # None if target not met

        result = deeper(target)
        return result if result else "0"
