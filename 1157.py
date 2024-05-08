class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.data = arr

        # sorted list of each characters positions
        self.pos = defaultdict(list)
        for i, a in enumerate(arr):
            self.pos[a].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        # at most 25 retries
        retry = min(25, len(self.data), right - left + 1)

        for i in range(retry):
            pick = randint(left, right)
            n    = self.data[pick]

            have = self.pos[n]
            if len(have) >= threshold:
                # binary search ...
                one  = bisect_left (have, left)
                two  = bisect_right(have, right, lo = one)
                if two - one >= threshold:
                    return n

        return -1
