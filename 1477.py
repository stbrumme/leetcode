class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        result = +inf

        prefix = [ 0 ] # prefix sum
        have   = []    # list of [ start, end ] for each subarray with sum == target
        for i, a in enumerate(arr):
            prefix.append(prefix[-1] + a)

            need = prefix[-1] - target
            pos  = bisect_left(prefix, need)
            # does it match the target sum ?
            if prefix[pos] == need:
                have.append(( pos, i ))

        # shortest subarray, beginning at pos
        size   = len(have)
        second = [ 0 ] * size + [ +inf ]
        for i in reversed(range(size)):
            a, b   = have[i]
            length = b - a + 1
            second[i] = min(second[i + 1], length)

        for i, (a, b) in enumerate(have):
            length = b - a + 1

            # skip if first part is already too long
            if length + 1 >= result:
                continue

            # earliest index of next match
            next = bisect_left(have, (b + 1, 0))
            if next == len(have): # no more matches
                break

            length += second[next]
            result  = min(result, length)

        return result if result != +inf else -1
