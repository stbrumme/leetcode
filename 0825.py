class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        all = defaultdict(int)
        for x in ages:
            all[x] += 1

        result = 0
        for x in ages:
            all[x] -= 1 # exclude yourself

            low = 0.5 * x + 7
            for y in all:
                if low < y <= x:
                    result += all[y]
            # third condition can be ignored because it's implied by the second condition

            all[x] += 1

        return result
