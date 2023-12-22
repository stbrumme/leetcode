class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low  = []
        same = []
        high = []
        for n in nums:
            if   n < pivot:
                low .append(n)
            elif n > pivot:
                high.append(n)
            else:
                same.append(n)

        return low + same + high
