class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(minutes, seconds):
            if minutes > 99 or seconds > 99:
                return +inf

            result = 0

            m1, m2 = divmod(minutes, 10)
            s1, s2 = divmod(seconds, 10)

            sequence = [ m1, m2, s1, s2 ]
            # trim leading zeros
            while sequence[0] == 0:
                sequence.pop(0)

            previous = startAt
            for x in sequence:
                # move
                if x != previous:
                    result  += moveCost
                    previous = x

                # push
                result += pushCost

            return result

        m, s = divmod(targetSeconds, 60)
        result = cost(m, s)

        # "wrong" format where seconds >= 60 (at most 99)
        if m > 0 and s < 40:
            result = min(result, cost(m - 1, s + 60))

        return result
