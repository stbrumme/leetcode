class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any((arr[i - 2] & 1) + (arr[i - 1] & 1) + (arr[i] & 1) == 3 for i in range(2, len(arr)))
