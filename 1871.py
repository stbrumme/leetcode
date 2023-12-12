class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active = defaultdict(set)
        for user, time in logs:
            active[user].add(time)

        result = [ 0 ] * k # one-based
        for a in active:
            minutes = len(active[a])
            if minutes <= k:
                result[minutes - 1] += 1 # one-based
        return result
