class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        size = len(obstacles)
        invalid = 999_999

        jumps = [ 1, 0, 1 ] # start in middle lane, it takes one jump to switch lane
        for o in obstacles:
            # invalidate if obstacle (encoded one-based, but my code is zero-based)
            if o > 0:
                jumps[o - 1] = invalid

            # find "fast" lane
            low = min(jumps)
            # update all lanes
            for i in range(3):
                # but not if an obstable exists
                if i != o - 1:
                    jumps[i] = min(low + 1, jumps[i]) # switch lane or stay in lane

        return min(jumps)
