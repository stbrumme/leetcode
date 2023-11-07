class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = { value: pos for pos, value in enumerate(arr2) }
        return sorted(arr1, key = lambda x : order[x] if x in order else 10_000 + x)
