class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        minutes = lambda t : 60 * int(t[:2]) + int(t[2:])

        all = defaultdict(list)
        for name, time in access_times:
            all[name].append(minutes(time))

        for a in all:
            current = sorted(all[a])
            for i in range(2, len(current)):
                if current[i] - current[i - 2] < 60:
                    yield a
                    break
