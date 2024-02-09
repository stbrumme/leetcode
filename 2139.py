class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result = 0

        while target > 0:
            # plus 1 to handle the lowest bit
            if target & 1:
                target -= 1
                result += 1
                continue

            # try to double if possible (lowest bit is always zero at this point)
            if maxDoubles > 0:
                result  += 1
                target //= 2
                maxDoubles -= 1
                continue

            # no more doubles available need plus 1 for the remainder
            result += target
            break

        return result - 1 # initial value is one
