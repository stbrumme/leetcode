class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        @cache
        def deeper(high, have):
            # consumed all digits
            if not high:
                return min_sum <= have <= max_sum # 1 if True

            first  = int(high[0])
            next   = high[1 :]
            # highest possible number (basically no limit)
            all    = "9" * len(next)
            # unrestricted if lower than the highest digit
            small  = sum(  deeper(all,  have + i) for i in range(first))
            # limit highest digit
            return small + deeper(next, have + first)

        one = deeper(str(int(num1) - 1), 0)
        two = deeper(        num2      , 0)
        return (two - one) % 1_000_000_007
