class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # prepend/append stop markers
        sides = [ 0 ] + sorted(cuts) + [ n ]

        @cache
        def deeper(left, right):
            # no cut, minimum length
            if left + 1 == right:
                return 0

            cost = sides[right] - sides[left]
            # try all cuts between left and right
            best = +inf
            for i in range(left + 1, right):
                best = min(best, cost + deeper(left, i) + deeper(i, right))
            return best

        return deeper(0, len(sides) - 1)
