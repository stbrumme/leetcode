class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        # there can only be one ...
        if k >= len(skills):
            return skills.index(max(skills))

        # edge case: first game decides
        if k == 1:
            return 0 if skills[0] > skills[1] else 1

        # brute force
        result = 0
        best   = skills[0]
        streak = 0
        for i, s in enumerate(skills[1 :], 1):
            if best < s:
                best   = s
                result = i
                streak = 1
            else:
                streak += 1
                if streak == k:
                    break

        return result
