class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors += colors[ : 2]
        return sum(a != b and b != c for a, b, c in zip(colors, colors[1 :], colors[2 :]))
