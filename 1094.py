class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta = defaultdict(int)
        for t in trips:
            delta[t[1]] += t[0]
            delta[t[2]] -= t[0]

        have = 0
        for d in sorted(delta):
            have += delta[d]
            if have > capacity:
                return False
        return True