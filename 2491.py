class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        result = 0

        size  = len(skill)
        teams = size // 2

        # all teams need equal total skill
        total = sum(skill)
        if total % teams != 0:
            return -1 # impossible
        total //= teams

        skill.sort()
        for i in range(teams):
            # match the lowest and highest player
            a = skill[i]
            b = skill[-i - 1]
            if a + b != total:
                return -1 # impossible

            # chemistry
            result += a * b

        return result
