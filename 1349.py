class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        height = len(seats)
        width  = len(seats[0])

        # convert seat map to bitmasks
        allowed = []
        for h in range(height):
            mask = 0
            for s in seats[h]:
                mask <<= 1
                mask  += 1 if s == "." else 0
            allowed.append(mask)

        # figure out which seat combinations are allowed behind each combination
        combinations = 1 << width
        compatible = [ [] for _ in range(combinations) ]

        for upper in range(combinations):
            # only relevant
            okay = False
            for a in allowed:
                if upper == 0 or ((upper & a) == upper):
                    okay = True
                    break

            if not okay:
                continue

            for lower in range(combinations):
                # noone must sit to the left or right
                if lower & (lower >> 1):
                    continue
                # noone must sit diagonally in front
                if ((upper << 1) | (upper >> 1)) & lower:
                    continue

                # only relevant
                for a in allowed:
                    if (lower & a) == lower:
                        compatible[upper].append(lower)
                        break

        @cache
        def deeper(row, upper):
            if row == height:
                return 0

            best = 0
            free = allowed[row]
            for c in compatible[upper]:
                if (c | free) == free:
                    best = max(best, deeper(row + 1, c) + c.bit_count())

            return best

        return deeper(0, 0)
