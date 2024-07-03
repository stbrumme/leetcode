class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        # count balls
        freq = defaultdict(int)
        for b in balls:
            freq[b] += 1

        # drop keys
        values = sorted(freq.values())
        del freq

        # boxes are at most one unit bigger than most rare value
        high = min(values) + 1

        # try large box sizes first
        for capacity in range(high, 0, -1):
            boxes = 0

            for f in values:
                # all boxes are either full (= capacity) or almost full (= capacity - 1)
                full, last = divmod(f, capacity)
                while last > 0:
                    # one more box that is almost full
                    boxes += 1
                    f     -= capacity - 1

                    # impossible
                    if f < 0:
                        boxes = -1
                        break

                    # try again
                    full, last = divmod(f, capacity)

                if boxes < 0:
                    break

                boxes += full

            if boxes > 0:
                return boxes
