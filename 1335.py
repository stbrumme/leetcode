class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs    = len(jobDifficulty)
        invalid = float("inf")

        @cache
        def deeper(done, days):
            if days == 0:
                return 0 if done == jobs else invalid
            if done + days > jobs:
                return invalid # prevent idle days
            if done == jobs:
                return 0

            best = invalid
            have = 0
            for i in range(done, jobs - days + 1):
                have = max(have, jobDifficulty[i])
                best = min(best, have + deeper(i + 1, days - 1))

            return best

        result = deeper(0, d)
        return -1 if result == invalid else result
