class Solution:
    def trimMean(self, arr: List[int]) -> float:
        five = len(arr) // 20
        arr  = sorted(arr)[five : -five]
        return sum(arr) / len(arr)
