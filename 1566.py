class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for a in range(len(arr)):
            ok = True
            for b in range(m):
                offset = a + b
                for c in range(k):
                    pos = offset + m * c
                    if pos >= len(arr) or arr[offset] != arr[pos]:
                        ok = False
                        break
            if ok:
                return True
        return False
