class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)

        capacity = max(weights)

        while True:
            have = 0            # load of current boat
            need = float("inf") # lowest excess of overloaded boats
            duration = 1
            for w in weights:
                have += w
                # overload
                if have > capacity:
                    need = min(need, have)
                    have = w
                    duration += 1
                    if duration > days:
                        break

            # done
            if duration <= days:
                return capacity

            capacity = need
