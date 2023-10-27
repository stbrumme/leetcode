class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        low    = 255
        high   =   0
        median =   0
        mode   =   0

        total  =   0
        sum_   = sum(count)
        max_   = max(count)
        mid1   = (sum_ + 1) // 2
        mid2   = (sum_ + 2) // 2
        seen   =   0

        for i, c in enumerate(count):
            # min/max
            if c != 0:
                low  = min(low,  i)
                high = max(high, i)

            # mean
            total += i * c

            # median
            if sum_ % 2 == 0:
                if seen < mid1 <= seen + c:
                    median += i
            if seen < mid2 <= seen + c:
                median += i
            seen  += c

            # mode
            if c == max_:
                mode = i

        return [ low, high, total  / sum_, median / (2 - (sum_ % 2)), mode ]
