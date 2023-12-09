class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # cryptic problems will lead to cryptic code ...
        return num + (t << 1)
