class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @lru_cache(maxsize = 200_000)
        def deeper(points, segments, inside = False):
            # too few points or too few segments
            if points   == 0:
                return 0
            if segments == 0:
                return 1

            if inside:
                one = deeper(points,     segments - 1, False) # a segment ends here
                two = deeper(points - 1, segments,     True)  # add point to current segment
            else:
                one = deeper(points - 1, segments,     False) # ignore this point
                two = deeper(points - 1, segments,     True)  # start new segment
                # "two" is computed the same way in both branches

            return (one + two) % 1_000_000_007

        return deeper(n, k)
