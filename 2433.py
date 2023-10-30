class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        last = 0
        for p in pref:
            yield last ^ p
            last = p
