class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0

        size = len(arr)
        nums = sorted([ ( a, i ) for i, a in enumerate(arr) ])

        # position in sorted array
        moved = [ 0 ] * size
        for new, (n, old) in enumerate(nums):
            moved[old] = new

        last = 0
        for i, (n, old) in enumerate(nums):
            # get new position of the number that was placed here
            new  = moved[i]
            last = max(last, new, old)

            # last element of a cycle
            if i == last:
                result += 1

        return result
