class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        size  = len(stones)
        inner = size - 2

        # maximum
        # find the range with the least stones (except one endpoint)
        # move a stone next to an endpoint, then move that endpoint next to the other endpoint
        high = max(stones[-1] - stones[1], stones[-2] - stones[0]) - inner

        # minimum:
        # find the range with the most stones
        low  = +inf
        left = 0
        for right, s in enumerate(stones):
            while s - stones[left] > size - 1:
                left += 1
            moves = size - (right - left + 1)

            # final move can be tricky if all stones are consecutive except an endpoint:
            # abcdef...g
            if moves == 1 and s - stones[left] == inner:
                moves = inner

            low = min(low, moves)

        return [ low, high ]
