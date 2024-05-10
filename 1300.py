class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()

        # the operation reduces the overall sum
        total = sum(arr)
        size  = len(arr)
        # can't decrement any element
        if total <= target:
            return arr[-1]

        for a in arr:
            # need an average in the not-yet-seen numbers less than the current number
            # however, Python's rounding causes headaches so I do it on my own
            average = target // size
            modulo  = target %  size
            # faster than modulo >= size // 2
            if modulo * 2 > size:
                average += 1

            if average <= a:
                return average

            target -= a
            size   -= 1
