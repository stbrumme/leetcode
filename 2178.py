class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1 or finalSum == 0:
            return []

        # 2,4,6,8,10,...
        result = [ 2 ]
        last   = total = 2
        while total < finalSum:
            last  += 2
            total += last
            result.append(last)

        # adjust last two numbers if too large
        if total > finalSum:
            total -= result.pop()
            total -= result.pop()
            result.append(finalSum - total)

        return result
