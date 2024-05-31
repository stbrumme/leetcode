class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # faster lookup
        pieces = { ( h, w ): price for h, w, price in prices }

        @cache
        def deeper(height, width):
            # try to sell the whole piece
            best = pieces.get(( height, width ), 0)

            # cut into two smaller chunks
            for h in range(height // 2):
                one  = deeper(         (h + 1), width)
                two  = deeper(height - (h + 1), width)
                best = max(best, one + two)

            for w in range(width  // 2):
                one  = deeper(height,         (w + 1))
                two  = deeper(height, width - (w + 1))
                best = max(best, one + two)

            return best

        return deeper(m, n)
