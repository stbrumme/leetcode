class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()

        xx = 1
        while xx <= bound:
            yy = 1
            while xx + yy <= bound:
                result.add(xx + yy)
                yy *= y
                if y == 1:
                    break

            xx *= x
            if x == 1:
                break

        return result
