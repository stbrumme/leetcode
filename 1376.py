class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = defaultdict(list)
        for i, m in enumerate(manager):
            sub[m].append(i)

        def deeper(id):
            if id not in sub:
                return 0

            slowest = 0
            for s in sub[id]:
                slowest = max(slowest, deeper(s))
            return slowest + informTime[id]

        return deeper(headID)
