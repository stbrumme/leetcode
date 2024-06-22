class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # find largest group of bars next to each other
        def best(bars):
            result  = 1
            current = 1
            bars.sort()
            for a, b in zip(bars, bars[1 :]):
                if a + 1 == b:
                    current += 1
                else:
                    current  = 1

                result = max(result, current)

            return result

        # scan horizontally and vertically
        h = best(hBars)
        v = best(vBars)

        # choose smaller group
        side = min(h, v) + 1
        return side * side
