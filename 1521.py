class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        result = +inf

        seen = set()
        for a in arr:
            # start new sequence
            next = set([ a ])
            result = min(result, abs(a - target))

            # append to sequence
            for s in seen:
                more = a & s

                result = min(result, abs(more - target))
                if result == 0:
                    return 0 # early exit

                # nice trick I saw in other solutions after submitting mine:
                # a & s <= a
                # therefore if "a" is already smaller than target
                # then there is no way it can contribute to a better result
                if more > target:
                    next.add(more)

            # prepare next round
            seen = next

        return result
