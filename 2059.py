class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        step = 0
        seen = set()
        todo = [ start ]
        while todo:
            next = set()
            for t in todo:
                seen.add(t)
                # done
                if t == goal:
                    return step
                # outside
                if t < 0 or t > 1000:
                    continue

                # keep going
                for n in nums:
                    if t + n not in seen:
                        next.add(t + n)
                    if t - n not in seen:
                        next.add(t - n)
                    if t ^ n not in seen:
                        next.add(t ^ n)

            step += 1
            todo  = next

        return -1 # impossible
