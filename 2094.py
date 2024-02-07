class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        reduced = [] # each digit at most three times
        freq = defaultdict(int)
        for d in digits:
            freq[d] += 1
            if freq[d] <= 3:
                reduced.append(d)

        result = set()

        for i1, d1 in enumerate(reduced):
            # no leading zero
            if d1 == 0:
                continue

            for i2, d2 in enumerate(reduced):
                # use distinct elements
                if i1 == i2:
                    continue

                for i3, d3 in enumerate(even):
                    # use distinct elements and ensure it's even
                    if i1 != i3 and i2 != i3 and (d3 & 1) == 0:
                        result.add(d1 * 100 + d2 * 10 + d3)

        return sorted(result)
