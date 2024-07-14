class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def deeper(left, right):
            # reject if degenerated
            if right - left < 2:
                return 0

            best = +inf
            for mid in range(left + 1, right):
                # three triangles (only "two" is fully triangulated, the others may be composites)
                one   = deeper(left, mid)
                two   = values[left] * values[mid] * values[right]
                three = deeper(mid, right)
                best  = min(best, one + two + three)

            return best

        return deeper(0, len(values) - 1)
