class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if not arr:
            return True

        for p in pieces:
            if all(arr[i] == p[i] for i in range(len(p))):
                return self.canFormArray(arr[len(p):], pieces)

        return False
