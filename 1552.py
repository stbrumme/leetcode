class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        # try to put balls into baskets and ensure minimum distance, return True if possible
        def put(distance):
            balls = m

            # always put a ball into the first basket
            prev = -10**11
            for p in position:
                if p - prev >= distance:
                    # store ball
                    prev   = p
                    balls -= 1
                    if balls == 0:
                        return True

            return False

        # binary search
        width = position[-1] - position[0]
        left  = 1
        right = width // (m - 1) # equidistant if enough baskets at good positions
        while left != right:
            mid = (left + right) // 2
            if put(mid):
                # balls could to be farther away
                left  = mid + 1
            else:
                # need shorter distance, not all balls fit into baskets
                right = mid

        return left if put(left) else left - 1
