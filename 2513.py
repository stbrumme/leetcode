class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def fits(limit):
            one = limit - limit // divisor1
            two = limit - limit // divisor2
            shared = limit - limit // lcm(divisor1, divisor2)
            return shared >= uniqueCnt1 + uniqueCnt2 and one >= uniqueCnt1 and two >= uniqueCnt2

        return bisect_left(range(10 * (uniqueCnt1 + uniqueCnt2)), True, key = fits)
