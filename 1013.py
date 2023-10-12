class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        third = total // 3

        completed = 0
        current = 0
        for a in arr:
            current += a
            if current == third:
                completed += 1
                current    = 0

        return completed >= 3
